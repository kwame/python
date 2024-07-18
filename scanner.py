import os
import sys
import subprocess
import shutil

def is_executable(file_path):
    executable_path = shutil.which(file_path)
    return executable_path and os.access(executable_path, os.X_OK)

def scan(network):
    subprocess.run(["sudo", "nmap", "-sT", "-O", network])

def main():
    file_to_check = "nmap"
    if is_executable(file_to_check):
        print(f"El binario de {file_to_check} si existe en el sistema")
        network = input("Ingresa el rango de red que deseas escanear: ")
        scan(network)
    else:
        print(f"{file_to_check} no está instalado, favor de instalarlo para proseguir.")

if __name__ == "__main__":
    main()
