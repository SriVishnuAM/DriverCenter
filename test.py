import subprocess
from runcommand import run_command
from dependencymanager import DependencyManager

manger = DependencyManager()

requirements= [
    "lsfusb",
    "lspci",
    "fastfetch",
    "curl",
    "sql"
]

manger.ensure_commands(requirements)

print(manger.dependencies)
