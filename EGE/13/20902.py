from ipaddress import ip_network


def main():
    ans = 0
    for ip in ip_network("172.16.80.0/255.255.248.0", 0):
        b_ip = bin(int(ip))[2:].zfill(32)
        if b_ip.count("1") % 2 == 0:
            ans += 1
    return ans


if __name__ == "__main__":
    print("ANS:", main())
