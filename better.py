# https://janakiev.com/blog/python-shell-commands/
import subprocess

process = subprocess.Popen(['nmap', f'192.168.43.15/28','-p 2-42', '--stats-every', '5s'],
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

while True:
    output = process.stdout.readline()
    if(len(output.strip())>0):
        print(output.strip())
    # Do something else
    return_code = process.poll()
    if return_code is not None:
        print('RETURN CODE', return_code)
        # Process has finished, read rest of the output
        for output in process.stdout.readlines():
            print(output.strip())
        break
