from rich.console import Console
from rich.progress import (
    Progress,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
    TimeElapsedColumn,
)

from dependencymanager import DependencyManager
from hardware import scan_hardware, os_info

console = Console()


def main():
    console.print("[bold cyan]Driver Manager for Linux[/bold cyan]\n")

    manager = DependencyManager()

    requirements = [
        "lsusb",
        "lspci",
        "fastfetch",
        "curl",
        "libapache2-mod-wsgi-py3",
    ]

    with Progress(
        TextColumn("[bold blue]{task.description}"),
        BarColumn(bar_width=40),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        console=console,
    ) as progress:

        task = progress.add_task("Checking dependencies...", total=100)

        # Check dependencies
        missing = manager.ensure_commands(requirements)
        progress.update(task, completed=50)

        # Install missing packages
        progress.update(task, description="Installing dependencies...")
        manager.resolve_dependencies(missing)

        # Finish
        progress.update(task, completed=100, description="Completed")

    console.print("[bold green]✓ Dependency check completed.[/bold green]\n")

    distro = os_info()

    if not distro:
        console.print("[bold red]Unsupported OS[/bold red]")
        return

    console.print(
        f"[bold green]Detected Distribution:[/bold green] [cyan]{distro}[/cyan]\n"
    )

    console.rule("[bold yellow]System Information[/bold yellow]")

    system = scan_hardware()
    console.print(system["system_info"])


if __name__ == "__main__":
    main()