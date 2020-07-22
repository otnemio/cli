import subprocess
import json
import re

json_var_ip={}
oo="" #variable to store output
ee="" #variable to store error
def runCommand(cmd,*argc):
    global oo
    global ee
    resout=""
    reserr=""
    process = subprocess.Popen([cmd,argc[0],argc[1]],
                           stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                           universal_newlines=True)

    while True:
        output = process.stdout.readline()
        error = process.stderr.readline()
        resout = resout+"\n"+str(output.strip())
        reserr = reserr+"\n"+str(error.strip())

        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output
            for output in process.stdout.readlines():
                resout = resout+"\n"+str(output.strip())
            for error in process.stderr.readlines():
                reserr = reserr+"\n"+str(error.strip())
            oo=resout.strip()
            ee=reserr.strip()
            break


#Json
# Data to be written
def extract_ip(ip_str):
    return re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ip_str).group()

for counter in range(1, 45, 5):
    print(f'nmap for 192.168.43.{counter}-{counter + 4}:')
    runCommand('nmap', f'192.168.43.{counter}-{counter + 4}', '-p 80,85,22', '-v')
    print("Output:")
    #print(oo)
    print("Error:")
    print(ee)

    line=""
    flagBlank=False
    for char in oo:
        if char!='\n':
            line+=char
        else:
            #print("-->"+line)
            if line.find("Nmap scan report for ")>=0:
                #print("ip-->" + line)
                ip_str=line[21:]
                #print(":::::ip string is "+ ip_str)
                ip=extract_ip(ip_str)
                json_var_ip[ip]= {}
            if (len(line) < 1) and flagBlank == False:
                #print("blank-->" + line + str(flagBlank))
                flagBlank = True
            elif (len(line) < 1) and flagBlank == True:
                #print("blank-->" + line + str(flagBlank))
                flagBlank = False
            if flagBlank is True and len(line)>0 and line[0].isdigit():
                #print(":::::::"+line)
                json_var_ip[ip][line.split(' ')[0]]=[line.split(' ')[1],line.split(' ')[2]]
            line=""


    flagStart=False
    flagPort=False

# Serializing json
json_object = json.dumps(json_var_ip, indent=4)

# Writing to sample.json
print("Json Output:\n")
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
print(json_object)

#runCommand('nmap','127.0.0.1','-O')
#runCommand('nmap','127.0.0.1','-F')
#runCommand('nmap','192.168.43.0/24','-sP')

#runCommand('nmap','192.168.43.221-225','-p 80-85', '-v')
#runCommand('nmap','127.0.0.1','-O')
#runCommand('nmap','127.0.0.1','-F')
#runCommand('nmap','192.168.43.0/24','-sP')
