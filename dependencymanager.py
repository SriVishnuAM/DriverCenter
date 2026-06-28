import subprocess
from runcommand import run_command
class DependencyManager:
    def check(self,command):
        output = run_command(["which",command])
        if output is None:
            return True
        else:
            return False