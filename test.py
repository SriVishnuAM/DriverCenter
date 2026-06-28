import subprocess
from runcommand import run_command
from dependencymanager import DependencyManager

manger = DependencyManager()

requirements= [
    "lsfusb",
    "lspci",
    "fastfetch",
    "sql",
    "yum"
]


manger.resolve_dependencies(requirements)


