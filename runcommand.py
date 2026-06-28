import subprocess

def run_command(command_list):
    """Safely runs a system command and handles missing utilities."""
    try:
        return subprocess.check_output(command_list, text=True)
    except FileNotFoundError:
        return None
    except subprocess.CalledProcessError as e:
        return None