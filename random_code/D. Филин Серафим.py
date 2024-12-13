def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    s = a[m - 1]
    sb = b[m - 1]
    for i in range(n):
        s = min(s, a[i] + sb)
        sb += b[i]

    for i in range(n - 1, m - 1, -1):
        s += min(a[i], b[i])
    return s


if __name__ == '__main__':
    for i in range(int(input())):
        print(main())
