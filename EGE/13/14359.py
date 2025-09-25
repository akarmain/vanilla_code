from ipaddress import ip_network


def main():
    for m in range(0, 33):
        net_1 = ip_network(f"157.127.172.56/{m}", 0)
        net_2 = ip_network(f"157.127.191.78/{m}", 0)
        if str(net_1.network_address) != str(net_2.network_address):
            b = str(net_1.netmask).split('.')
            c = 0
            for d in b:
                c += bin(int(d)).count("1")
            return c


if __name__ == "__main__":
    print("ANS:", main())
