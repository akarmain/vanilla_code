from ipaddress import ip_network, ip_address
def main():
    net = ip_network("5.2.5.0/255.255.0.0", 0)
    ans = 0
    for ip in net.hosts():
        ip_2 = bin(int(ip))[2:].zfill(32)
        print(ip_2)
        if ip_2.count("0") % 25 == 0:
            ans+=1
    return ans

if __name__ == "__main__":
    print("ANS:", main())
