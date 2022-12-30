import psutil

#result01=psutil.cpu_times()
#print(result01)
'''
result02=psutil.cpu_stats()
print(result02)

result03=psutil.cpu_freq()
print(result03)

result04=psutil.disk_partitions()
print(result04)

result05=psutil.net_io_counters(pernic=True)
print(result05)
'''

network_stats=psutil.net_io_counters(pernic=False)
bytes_sent=getattr(network_stats, 'bytes_sent')
bytes_recv=getattr(network_stats, 'bytes_recv')

print("Bytes Sent = {0} | Bytes Received = {1}".format(bytes_sent,bytes_recv))