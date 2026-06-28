import subprocess
from runcommand import run_command
from dependencymanager import DependencyManager

manger = DependencyManager()

requirements= [
    "lsfusb",
    "lspci",
    "fastfetch",
<<<<<<< HEAD
    "sql",
    "yum"
]


manger.resolve_dependencies(requirements)


=======
    "curl",
    "sql"
]

manger.resolve_dependencies(commands)


>>>>>>> refs/remotes/orgin/main
