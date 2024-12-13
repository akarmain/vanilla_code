def main():
    n = int(input())
    a = list(map(int, input().split()))
    su = set({0})
    s = 0
    f = False
    for i in range(n):
        if i % 2 == 0:
            s += a[i]
        else:
            s -= a[i]
        if s in su:
            f = True
            break
        else:
            su.add(s)
    print("YES" if f else "NO")


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
