import argparse

from hardware import (
    scan_hardware,
    install_flow,
    search_packages
)


def print_report():
    data = scan_hardware()

    
    print("DRIVER CENTER - HARDWARE REPORT")
   

    print("\n=== SYSTEM INFO ===")
    print(data["system_info"])

    print("\n=== PCI DEVICES ===")
    print(data["pci_devices"])

    print("\n=== USB DEVICES ===")
    print(data["usb_devices"])

    print("\n=== STORAGE DEVICES ===")
    print(data["storage_devices"])

    print("\n=== IP INFORMATION ===")
    print(data["ip_info"])

    print("\n=== HOSTNAME ===")
    print(data["hostname"])

    print("\n=== OS INFORMATION ===")
    print(data["os_info"])

    print("\n=== DISK USAGE ===")
    print(data["disk_usage"])

    print("\n=== LOADED MODULES ===")
    print(data["loaded_modules"])

    print("\n=== AUDIO DEVICES ===")
    print(data["audio_devices"])

    print("\n=== GRAPHICS ===")
    print(data["graphics"])

    print("\n=== LOADED MODULES ===")
    print(data["loaded_modules"])


def main():
    parser = argparse.ArgumentParser(
        prog="driver-center",
        description="Driver Center CLI"
    )

    sub = parser.add_subparsers(dest="command")

    sub.add_parser("scan")
    sub.add_parser("install")

    search = sub.add_parser("search")
    search.add_argument("package")

    args = parser.parse_args()

    if args.command == "scan":
        print_report()

    elif args.command == "install":
        install_flow()

    elif args.command == "search":
        packages = search_packages(args.package)

        if packages:
            print("\nMatching Packages:\n")
            for pkg in packages:
                print(pkg)
        else:
            print("No packages found.")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()