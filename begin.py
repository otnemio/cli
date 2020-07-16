import subprocess 

oo="" #variable to store output
ee="" #variable to store error
def runCommand(cmd,arg1,arg2):
    global oo
    global ee
    resout=""
    reserr=""
    process = subprocess.Popen([cmd,arg1,arg2], 
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

runCommand('nmap','192.168.43.225-230','-p 10-30')
print("Output:")
print(oo)
print("Error:")
print(ee)
#runCommand('nmap','127.0.0.1','-O')
#runCommand('nmap','127.0.0.1','-F')
#runCommand('nmap','192.168.43.0/24','-sP')


