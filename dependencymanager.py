import json
from runcommand import run_command
class DependencyManager:

    def __init__(self):       
        with open("dependencies.json", "r") as file:
            self.dependencies = json.load(file)

    def command_exists(self,command):
        output = run_command(["which",command])
        if output:
            return True
        else:
            return False
    
    def ensure_commands(self,commands):
        missing = []
        for item in commands:
            if  not (self.command_exists(item)):
                missing.append(item)
        return missing
    
    def get_package(self,command):
        try:
            return self.dependencies[command]
        except KeyError:
            return None
    
    def get_packages(self,commands):
        packages = []
        for item in commands:
            package = self.get_package(item)
            if package:
                packages.append(package)
        return packages

    def install_package(self,package):
        try:
            run_command(["sudo", "apt" ,"install",package])
        except:
            print("Error occured while trying to install",package)
    
    def install_packages(self,packages):
        for item in packages:
            self.install_package(item)

    def resolve_dependencies(self,requirements):
        missing = self.ensure_commands(requirements)
        if missing:
            packages = self.get_packages(missing)
            print("The following packages are missing \n",packages,"install them all? (Y/N)")
            answer = input().lower().strip()
            while(True):
                if answer == "y":
                    self.install_packages(packages)
                    return
                elif answer == "n":
                    return 
                else:
                    print("Please Enter Either Y or N")
                    answer = input().lower().strip()




        
