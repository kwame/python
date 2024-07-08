import os
import sys
import subprocess
print ("this is a script that scans your local network for ips and it's listening ports")

def test_binary():
    try: 
    #    nmap = "/usr/bin/nmap"
    #    check_scanner = os.path.isfile(nmap)
    #    print(check_scanner)
        with open('/usr/local/bin/nmap', 'r') as file:
            print("The nmap binary exists")
    except FileNotFoundError:
        print("The nmap binary does not exist, please install it")

test_binary()

def run_nmap(target):
    try:
        result = subprocess.run(["sudo /usr/local/bin/nmap -sT -O", target], capture_output=True, text=True)

        if result.returncode == 0:
            print("nmap scan successful:")
            print(result.stdout)
        else:
            print("nmap scan failed:")
            print(result.stderr)
    except Exception as e:
        print(f"An error ocurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python ip-scanner.py <network range>")
        sys.exit(1)

    target = sys.argv[1]
    run_nmap(target)