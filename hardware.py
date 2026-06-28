import subprocess

def scan_hardware():
    try:
        pci_output = subprocess.check_output(["lspci", "-k"], text=True)
    except FileNotFoundError:
        pci_output = "lspci command not found. Install it using 'sudo apt install pciutils'."

    try:
        system_info = subprocess.check_output(["fastfetch"], text=True)
    except FileNotFoundError:
        system_info = "fastfetch command not found. Install it using 'sudo apt install fastfetch'."

    return pci_output, system_info