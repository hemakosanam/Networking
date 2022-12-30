import socket
import subprocess
import sys

from datetime import datetime

#Blank your screen
subprocess.call('clear',shell=True)

#Ask for input
remoteServer=input("Enter a remote host to scan")
remoteServerIP=socket.gethostname(remoteServer)

#print a nice banner with information on which host we are about to scan
print("_" *60)
print("please wait,scanning remote host", remoteServerIP)

print("_"*60)

t1=datetime.now()

try:
    for port in range(1,1500):
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result=sock.connect_ex((remoteServerIP, port))
        if result ==0:
            print("port {}:  open".format(port))
            sock.close()
except keyboardInterrupt:
    print("You pressed Ctrl+c")
    sys.exit()
except socket.gaierror:
    print("hostname could not be resolved.exiting")
    sys.exit()
except socket.error:
    print("couldn't connect to server")
    sys.exit()
        