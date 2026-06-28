from rich.console import Console
import platform
import time
with Console().status("Checking"):
    time.sleep(5)
Console().print("Done")

print(platform.freedesktop_os_release()["ID"])