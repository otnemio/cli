import subprocess 

def runCommand(cmd,arg1,arg2):
    process = subprocess.Popen([cmd,arg1,arg2], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

    while True:
        output = process.stdout.readline()
        print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output 
            for output in process.stdout.readlines():
                print(output.strip())
            break

runCommand('nmap','192.168.43.225-230','-p 10-30')
#runCommand('nmap','127.0.0.1','-O')
#runCommand('nmap','127.0.0.1','-F')
