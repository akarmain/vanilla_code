from ipaddress import ip_network


def main():
    ans = set()
    for m in range(0, 33):
        net = ip_network(f"218.48.192.56/{m}", 0)
        if str(net.network_address) == "218.48.192.0":
            if len(list(net.hosts())) >= 500:
                ans.add(str(net.netmask).split(".")[2])
    return len(ans)


if __name__ == "__main__":
    print("ANS:", main())
