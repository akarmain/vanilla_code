from ipaddress import ip_network

net = ip_network("17.234.25.1/255.255.224.0", strict=False)
b = net.broadcast_address

print(b)  
print(sum(map(int, str(b).split("."))))  # 537
