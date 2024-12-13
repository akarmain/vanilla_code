def f(d, arr, n, p):
    x = 1
    for i in range(n - 1, -1, -1):
        p -= arr[i] * x
        x += d
    return p >= 0


def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    p = int(input())
    l = 0
    r = 10 ** 18
    while l + 1 < r:
        m = (l + r) // 2
        if f(m, arr, n, p):
            l = m
        else:
            r = m
    print(l)


if __name__ == '__main__':
    main()
