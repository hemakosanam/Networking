# import socket moduke

import socket

#create a socket object
s=socket.socket()

port=40674

s.connect(('127.0.0.1',port))

print(s.recv(1024))

s.close()