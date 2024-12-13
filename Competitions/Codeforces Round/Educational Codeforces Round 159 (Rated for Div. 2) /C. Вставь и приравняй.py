from math import gcd


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    g = a[-1] - a[0]
    for i in range(n - 1):
        g = gcd(g, a[i + 1] - a[i])
    s = 0
    for i in range(n):
        s += (a[-1] - a[i]) // g
    for i in range(n - 1):
        if (a[-1 - i] - a[-1 - i - 1] != g):
            s += i
            break
    else:
        s += n
    return s


if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())
