import os
import sys
import subprocess

network = input("Ingresa el rango de red que deseas escanear: ")

scan = subprocess.run(["sudo", "nmap", "-sT", "-O", network])

print(scan.stdout)