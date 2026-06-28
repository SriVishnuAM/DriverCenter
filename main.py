import subprocess

def run_command(command_list):
    """Safely runs a system command and handles missing utilities."""
    try:
        return subprocess.check_output(command_list, text=True)
    except FileNotFoundError:
        return f"Error: Command '{' '.join(command_list)}' is not installed."
    except subprocess.CalledProcessError as e:
        return f"Error running command: {e}"

def scan_hardware():
    # Safely grab outputs using our helper function
    pci_output = c
    system_info = run_command(["fastfetch"])
    usb_devices = run_command(["lsusb"])
    storage_devices = run_command(["lsblk"])

    return {
        "system_info": system_info,
        "pci_devices": pci_output,
        "usb_devices": usb_devices,
        "storage_devices": storage_devices,
    }

def main():
    data = scan_hardware()

    print("=== System Info ===")
    print(data["system_info"])

    print("\n=== PCI Devices ===")
    print(data["pci_devices"])

    print("\n=== USB Devices ===")
    print(data["usb_devices"])

    print("\n=== Storage ===")
    print(data["storage_devices"])

if __name__ == "__main__":
    main()