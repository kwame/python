import os
print ("this is a script that scans your local network for ips and it's listening ports")

try: 
#    nmap = "/usr/bin/nmap"
#    check_scanner = os.path.isfile(nmap)
#    print(check_scanner)
    with open('/usr/bin/nmap', 'r') as file:
        print("The nmap binary exists")
except FileNotFoundError:
    print("The nmap binary does not exist, please install it")

