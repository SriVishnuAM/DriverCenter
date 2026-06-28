import subprocess
import difflib


def run_command(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout.strip()
    except Exception as e:
        return str(e)



def scan_hardware():

    return {
        "system_info": run_command(["fastfetch"]),
        "pci_devices": run_command(["lspci", "-k"]),
        "usb_devices": run_command(["lsusb"]),
        "storage_devices": run_command(["lsblk"]),
        "ip_info": run_command(["ip", "addr"]),
        "kernel": run_command(["uname", "-r"]),
        "hostname": run_command(["hostname"]),
        "os_info": run_command(["cat", "/etc/os-release"]),
        "disk_usage": run_command(["df", "-h"]),
        "loaded_modules": run_command(["lsmod"]),
        "audio_devices": run_command(["aplay", "-l"]),
        "graphics": run_command(["lshw", "-c", "video"]),
        "installed_packages": run_command(["dpkg", "-l"])
    }


def search_packages(query):

    result = subprocess.run(
        ["apt-cache", "search", query],
        capture_output=True,
        text=True
    )

    packages = []

    for line in result.stdout.splitlines():
        if " - " in line:
            packages.append(line.split(" - ")[0])

    return packages



def apt_install(package):

    result = subprocess.run(
        ["sudo", "apt", "install", "-y", package]
    )

    return result.returncode


def install_flow():

    while True:

        package = input("\nPackage to install (or exit): ").strip()

        if package.lower() == "exit":
            return

        code = apt_install(package)

        if code == 0:
            print("\nInstalled Successfully!")
            return

        print("\nPackage not found.")

        packages = search_packages(package)

        if not packages:

            retry = input(
                "\nNo similar packages found.\nRetry? (y/n): "
            )

            if retry.lower() == "y":
                continue

            return

        matches = difflib.get_close_matches(
            package,
            packages,
            n=10,
            cutoff=0.3
        )

        if not matches:
            matches = packages[:10]

        print("\nSuggested Packages\n")

        for i, pkg in enumerate(matches, 1):
            print(f"{i}. {pkg}")

        choice = input(
            "\nSelect package number (0 to retry): "
        )

        if not choice.isdigit():
            continue

        choice = int(choice)

        if choice == 0:
            continue

        if 1 <= choice <= len(matches):

            code = apt_install(matches[choice - 1])

            if code == 0:
                print("\nInstalled Successfully!")
                return

            print("\nInstallation Failed.")