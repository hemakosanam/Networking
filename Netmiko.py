from netmiko import ConnectHandler
CSR = {
    "device_type":"cisco_ios",
    #"device_type":"juniper_junos",
    #"ip":"sandbox-iosxe-latest-1.cisco.com",
    "ip":"sandbox-iosxe-recomm-1.cisco.com",
    #"port":204,
    "username": "developer",
    "password":"C1sco12345"
 } 
net_connect = ConnectHandler(**CSR)

output = net_connect.send_command('show ip int brief')
print(output)
'''
output_clock=net_connect.send_command('show clock ')
print(output_clock)

output_router=net_connect.send_command('show ip ro')
print(output_router)

output_runconfig=net_connect.send_command('show run')
print(output_runconfig)

#output_runhost = net_connect.send_command('show run | i host')
#print(output_runhost)
'''

net_connect.disconnect()