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
    system_info = subprocess.check_output(["fastfetch"], text=True)
    pci_devices = subprocess.check_output(["lspci", "-k"], text=True)
    usb_devices = subprocess.check_output(["lsusb"], text=True)
    storage = subprocess.check_output(["lsblk", "-o", "NAME,SIZE,TYPE,MOUNTPOINT,FSTYPE"], text=True)
    cpu = subprocess.check_output(["lscpu"], text=True)memory = subprocess.check_output(["free", "-h"], text=True)
    network = subprocess.check_output(["ip", "addr"], text=True)hostname = subprocess.check_output(["hostname"], text=True).strip()
    os_info = subprocess.check_output(["cat", "/etc/os-release"], text=True)
    disk_usage = subprocess.check_output(["df", "-h"], text=True)
    loaded_modules = subprocess.check_output(["lsmod"], text=True)
    audio_devices = subprocess.check_output(["aplay", "-l"], text=True)
    graphics = subprocess.check_output(["lshw", "-c", "video"],text=True)

    return {
        "system_info": system_info,
        "pci_devices": pci_devices,
        "usb_devices": usb_devices,
        "storage_devices": storage,
        "ip_info": network,
        "os_info":os_info ,
        "disk_usage": disk_usage,
        "loaded_modules":loaded_modules ,
        "audio_devices": audio_devices,
        "graphics": graphics,
        
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