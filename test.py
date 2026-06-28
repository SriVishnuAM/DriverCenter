import subprocess
from runcommand import run_command
from dependencymanager import DependencyManager

manger = DependencyManager()

commands = [
    "lsfusb",
    "lspci",
    "fastfetch",
    "curl",
    "sql"
]

manger.resolve_dependencies(commands)


