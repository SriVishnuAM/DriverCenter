import argparse
from colorama import Fore, Style, init
import rich
from rich.console import Console
from dependencymanager import DependencyManager as manager
from hardware import (
    scan_hardware,
    install_flow,
    search_packages,
    os_info,
)


""" def print_report():
    data = scan_hardware()

    
    print("DRIVER CENTER - HARDWARE REPORT")

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
"""

def main():
    print("DRIVER MANAGER FOR LINUX")
    init(autoreset=True)
    #with Console().status("Checking dependencies..."):
    #   missing = manager.ensure_commands(commands)

    #Console.print("✓ Done!")
    os = os_info()
    if os == False:
        print("Unsupported OS")
    else:
        print(f"{Fore.RED}Your OS is based on {os_info()} distribution{Style.RESET_ALL}")
    print("\n=== SYSTEM INFO ===")
    print(scan_hardware()["system_info"])

if __name__ == "__main__":
    main()