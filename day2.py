import os, ipaddress
 
os.system('cls') #os.system will clear the console at the start of the execution

while True:
    ip=input('enter ip address: ');
    try:
        print(ipaddress.ip_address(ip));
        print('IP Valid');
    except:
        print('-' *50)
        print('IP is not valid');
    finally:
        if ip=='mango':
            print('Script Finished')
            break

#<package :ipaddress>.<ip_address>.<attribute : ip>