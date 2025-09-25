from ipaddress import ip_network


def main():
    ans = 0
    for ip in ip_network("112.160.0.0/255.240.0.0", 0):
        b_ip = bin(int(ip))[:2].zfill(32)
        if b_ip.count("1") % 5 == 0:
            ans += 1
    return ans


if __name__ == "__main__":
    print("ANS:", main())
