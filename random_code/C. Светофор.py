n, m, s, ans = "", "", "", 0


def get_count(i):
    return s[i:].index("g")


def main():
    global n, m, s, ans
    n, m = map(str, input().split())
    s = list(map(lambda x: 0 if x == "g" else 2 if x == "r" else 1, input()))
    n = int(n)
    s += s
    print(s)

if __name__ == "__main__":
    for i in range(int(input())):
        main()
