import subprocess
from runcommand import run_command
from dependencymanager import DependencyManager

manger = DependencyManager()

def checker(command):
    output =  manger.check(command)
    if output:
        print("Found")
    else:
        print("Not Found")

checker("lsusb")

