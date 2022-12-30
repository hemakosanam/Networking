'''
import scapy.all as scapy

request=scapy.ARP()
print(request.summary())

print(request.show())
'''
'''
from scapy.all import *
ip=IP()
print(ip)
print(ip.show())
'''
'''
from scapy.all import *
my_frame=Ether() / IP()
print(my_frame)
print(my_frame.show())
'''
'''
from scapy.all import *
s= IP(dst ="google.com")/ICMP()
print(s.show())
'''

import pexpect
print(pexpect.run('echo hello'))
