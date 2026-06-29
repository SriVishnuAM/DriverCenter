from rich.console import Console
from rich.progress import (
    Progress,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
    TimeElapsedColumn,
)
from rich.text import Text
import pyfiglet

from dependencymanager import DependencyManager
from hardware import scan_hardware, os_info

console = Console()


def print_banner():
    """Print application banner."""

    terminal_width = console.size.width

    banner = pyfiglet.figlet_format(
        "Hades",
        font="slant",
        width=terminal_width,
        justify="center",
    )

    console.print(banner, style="bold bright_red", overflow="ignore")

    subtitle = Text(
        "Linux Driver Manager",
        style="bold cyan",
        justify="center",
    )
    console.print(subtitle)

    console.rule(style="bright_black")


def main():
    print_banner()

    manager = DependencyManager()

    requirements_hardware = [
    "fastfetch",
    "lspci",
    "lsusb",
    "lsblk",
    "lscpu",
    "free",
    "ip",
    "hostname",
    "df",
    "lsmod",
    "aplay",
    "lshw",
    "curl",
    "python3",
    ]
    requirements_python = [
    "rich",
    "pyfiglet",
    ]
    with Progress(
        TextColumn("[bold cyan]{task.description}"),
        BarColumn(bar_width=None),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        console=console,
    ) as progress:

        task = progress.add_task(
            "Checking dependencies...",
            total=100,
        )

        missing = manager.ensure_commands(requirements_hardware)

        progress.update(task, completed=50)

        if missing:
            progress.update(
                task,
                description="Installing dependencies...",
            )
            manager.resolve_dependencies(missing)

        progress.update(
            task,
            completed=100,
            description="Completed",
        )

    console.print()

    console.print(
        "[bold green]✓ Dependency check completed.[/bold green]"
    )

    distro = os_info()

    if not distro:
        console.print("[bold red]Unsupported Linux distribution.[/bold red]")
        return

    console.print(
        f"[bold green]Detected Distribution:[/bold green] [cyan]{distro}[/cyan]"
    )

    console.print()

    console.rule("[bold yellow]System Information[/bold yellow]")

    system = scan_hardware()

    console.print(system["system_info"],width=500)


if __name__ == "__main__":
    main()