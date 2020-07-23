# https://janakiev.com/blog/python-shell-commands/
# https://www.tecmint.com/nmap-command-examples/

import subprocess
import re
import json

# variable for json output
json_var_ip={}

# Data to be written
def extract_ip(ip_str):
    return re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ip_str).group()

# run command to print output and store necessary part in a json format variable
def runcommand(cmd, *argc):
    ip_info=""
    process = subprocess.Popen([cmd, argc],
                               stdout=subprocess.PIPE,
                               universal_newlines=True)
    while True:
        output = process.stdout.readline()
        #Only print the output lines required
        if len(output.strip()) > 0:
            if output.find("Scan Timing: About") >= 0:
                start=output.find("About")+6 # starting location of percent done
                end=output.find("done")-1 # ending location of percent done
                print(f"::{output.strip()[start:end]}::")
            elif output.find("Stats:") >= 0:  # no need to print
                pass
            elif output.find("Nmap scan report for") >= 0:  # ip address which has been scanned
                extracted_ip=extract_ip(output.strip())
                print(f"::{extracted_ip}::")
                json_var_ip[extracted_ip] = {}
            else:
                print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output,
            # nothing remains to be read from stdout so commented these lines
            # for output in process.stdout.readlines():
            #    print(output.strip())
            break


# this is the function being called first
runcommand('nmap', f'192.168.43.1-5 -p 22-30 --stats-every 5s')

# Serializing json
json_object = json.dumps(json_var_ip, indent=4)

# Writing to sample.json
print("Json Output:\n")
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
print(json_object)

