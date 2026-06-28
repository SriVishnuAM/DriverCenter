import subprocess
from runcommand import run_command
class DependencyManager:
    def check(self,command):
        output = run_command(["which",command])
        if output:
            return True
        else:
            return False
    
    def ensure_commands(self,list):
        missing = []
        for item in list:
            if  not (self.check(item)):
                missing.append(item)
        print(missing)        
            