import socket

#create a socket object
s=socket.socket()
print("socket successfully created")


#define the port numbe
port=40674                  #


s.bind(('',port))

print("socket binded to %s" %(port))
s.listen(5)
print("socket is listening")

while True:

    # Establish connection with client
    c, addr=s.accept()           #single line,multivariable assignment
    
    print(c)
    print('Got connection from', addr)
    print(c)
    c.send(b'Thank you for connecting')
    c.close()