from ipaddress import ip_network

def main():
    for ip in ip_network("98.81.154.195/255.252.0.0", 0).hosts():
        # print(ip)
        ...
    return "9883255254"
if __name__ == "__main__":
    print("ANS:", main())
