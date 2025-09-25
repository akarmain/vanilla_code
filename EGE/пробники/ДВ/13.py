from ipaddress import ip_network

def main():
    net = ip_network("143.168.72.213/255.255.255.240", 0)
    print(list(net.hosts())[-1])
    ...


if __name__ == "__main__":
    print("ANS:", main())
