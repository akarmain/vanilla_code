from ipaddress import ip_network
def main():
    for m in range(0, 33):
        net1 = ip_network(f"157.220.185.237/{m}", 0)
        net2 = ip_network(f"157.220.184.230/{m}", 0)
        if net1.network_address == net2.network_address:
            print(m)
    ...

if __name__ == "__main__":
    print("ANS:", main())
