import os
import sys
import subprocess
import shutil

def is_executable(file_path):
    executable_path = shutil.which(file_path)
 
    if executable_path and os.access(executable_path, os.X_OK):
        return True
    else:
        return False

def scan():
    range = subprocess.run(["sudo", "nmap", "-sT", "-O", network])


file_to_check = "nmap"
if is_executable(file_to_check):
    print(f"El binario de {file_to_check} si existe en el sistema")
    network = input("Ingresa el rango de red que deseas escanear: ")
    scan()

else:
    print(f"{file_to_check} no está instalado, favor de instalarlo para proseguir.")

