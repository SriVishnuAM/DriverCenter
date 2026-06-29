import subprocess
import json
from runcommand import run_command
class DependencyManager:

    def __init__(self):       
        with open("dependencies.json", "r") as file:
            self.dependencies = json.load(file)
            self.cache = {}

    def command_exists(self,command):
            if command in self.cache:
                if self.cache[command] == True:
                    return True
                else:
                    return False
            else:
                output = run_command(["which",command])
                if output:
                    self.cache[command] = True
                    return True
                else:
                    self.cache[command] = False
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
        
    def get_command(self,package):
        found_key = None
        for key, val in  self.dependencies.items():
            if val == package:
                return key # Stop searching immediately
        return None # FallBack

    def get_packages(self,commands):
        packages = []
        for item in commands:
            package = self.get_package(item)
            if package!= None:
                packages.append(package)
            else:
                print("Package not found for in dependencies.json:",item)
        return packages

    def install_package(self,package):
        try:
            subprocess.run(["sudo", "apt" ,"install","-y",package])
            command = self.get_command(package)
            if command:
                self.cache[command] = True
        except:
            print("Error occured while trying to install",package)
            command = self.get_command(package)
            if command:
                self.cache[command] = False
    
    def install_packages(self,packages):
        for item in packages:
            self.install_package(item)

    def resolve_dependencies(self,requirements):
        missing = self.ensure_commands(requirements)
        if missing == [] :
            packages = self.get_packages(missing)
            if packages is not None:
                print("No package found to be install.")
                return
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
        else:
            print("All Packages and Commands are Present")

    def refresh_cache(self):
        self.cache.clear()

        




        
