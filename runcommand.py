import subprocess

def run_command(command_list):
    """Safely runs a system command and handles missing utilities."""
    try:
        return subprocess.check_output(command_list, text=True)
    except FileNotFoundError:
        return f"Error: Command '{' '.join(command_list)}' is not installed."
    except subprocess.CalledProcessError as e:
        return f"Error running command: {e}"