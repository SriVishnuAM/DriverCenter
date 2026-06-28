import subprocess
from runcommand import run_command

print(run_command(["which", "lsusb"]))
print(run_command(["which", "lsfusb"]))