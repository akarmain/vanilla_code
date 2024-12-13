def main():
    n = int(input())
    a = list(map(int, input().split()))
    l = [0] * n
    l[0] = a[0]
    for i in range(1, n):
        l[i] = max(a[i], l[i - 1] - 1)
    r = [0] * n
    r[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        r[i] = max(a[i], r[i + 1] - 1)

    b = [str(max(l[i], r[i])) for i in range(n)]
    return " ".join(b)


if __name__ == '__main__':
    print(main())
