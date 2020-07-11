import subprocess

mycmd="nmap"
myarg1=input("Enter ip range ") #"192.168.1.1-5"
myarg2="-p " +input("Enter port range ") #"10-30"

out=subprocess.check_output([mycmd,myarg1,myarg2])
print(out.decode("utf-8"))