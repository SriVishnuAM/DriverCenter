import json
from runcommand import run_command
class DependencyManager:

    def __init__(self):       
        with open("dependencies.json", "r") as file:
            self.dependencies = json.load(file)

    def check(self,command):
        output = run_command(["which",command])
        if output:
            return True
        else:
            return False
    
    def ensure_commands(self,commands):
        missing = []
        for item in commands:
            if  not (self.check(item)):
                missing.append(item)
        return missing
    
    def get_package(self,command):
        return self.dependencies[command]
