# https://janakiev.com/blog/python-shell-commands/
# https://www.tecmint.com/nmap-command-examples/
# https://avleonov.com/2018/03/11/converting-nmap-xml-scan-reports-to-json/

import subprocess
import json
import xmltodict


# run command to print output and store necessary part in a json format variable
def runcommand(cmd, *argc):
    ip_info=""
    process = subprocess.Popen([cmd, argc],
                               stdout=subprocess.PIPE,
                               universal_newlines=True)
    while True:
        output = process.stdout.readline()
        #Only print the output lines necessary
        if len(output.strip()) > 0:
            if output.find("Ping Scan Timing: About") >= 0:         # extract percent for Ping Scan progress
                start = output.find("About") + 6                    # starting location of percent done
                end = output.find("done") - 1                       # ending location of percent done
                print(f"Ping::{output.strip()[start:end]}::")       # percent done
            elif output.find("Stealth Scan Timing: About") >= 0:    # extract percent for Stealth Scan progress
                start = output.find("About") + 6                    # starting location of percent done
                end = output.find("done") - 1                       # ending location of percent done
                print(f"Stealth::{output.strip()[start:end]}::")    # percent done
        return_code = process.poll()                                # fetch return code from Process
        if return_code is not None:
            print('RETURN CODE', return_code)
            # for output in process.stdout.readlines():             # Process has finished, read rest of the output,
            #    print(output.strip())                              # nothing remains to be read from stdout so commented these lines
            break


# this is the function being called first
runcommand('nmap', f'192.168.43.1-60 -p 22,23,80 --stats-every 2s --oX nmap_output.xml')

f = open("nmap_output.xml")
xml_content = f.read()
f.close()
json_object = json.dumps(xmltodict.parse(xml_content) , indent=4, sort_keys=True)


# Writing to sample.json
print("Json Output:\n")
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
print(json_object)
