import subprocess
from runcommand import run_command
from dependencymanager import DependencyManager

manger = DependencyManager()

commands = [
    "lsfusb",
    "lspci",
    "fastfetch"
]

manger.ensure_commands(commands)
print(manger.get_package("fastfsetch"))
