import os
import sys
import subprocess

nmap_binary = os.path.isfile(/)

network = input("Ingresa el rango de red que deseas escanear: ")

def scan():
    range = subprocess.run(["sudo", "nmap", "-sT", "-O", network])

scan()
