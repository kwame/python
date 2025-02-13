import re
log_file = "/var/log/syslog"
error_file = "errors.log"

with open(log_file, "r") as infile, open(error_file, "w") as outfile: 
    for line in infile:
        if "ERROR" or "WARNING" in line:
            outfile.write(line)

print(f"Extracted errors saved to {error_file}")