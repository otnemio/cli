import subprocess
import json

oo="" #variable to store output
ee="" #variable to store error
def runCommand(cmd,*argc):
    global oo
    global ee
    resout=""
    reserr=""
    process = subprocess.Popen([cmd,argc[0],argc[1],argc[2]],
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

runCommand('nmap','192.168.43.225-226','-p 80-85','-v')
print("Output:")
#print(oo)
line=""
flagBlank=False
for char in oo:
    if char!='\n':
        line+=char
    else:
        #print("-->"+line)
        if line.find("Nmap scan report for ")>=0:
            print("ip-->" + line)
            print("ip is "+line[21:])
        if (len(line) < 1) and flagBlank == False:
            print("blank-->" + line + str(flagBlank))
            flagBlank = True
        elif (len(line) < 1) and flagBlank == True:
            print("blank-->" + line + str(flagBlank))
            flagBlank = False
        if flagBlank is True:
            print(":::::::"+line)
        line=""
flagStart=False
flagPort=False

print("Error:")
print(ee)
#runCommand('nmap','127.0.0.1','-O')
#runCommand('nmap','127.0.0.1','-F')
#runCommand('nmap','192.168.43.0/24','-sP')
