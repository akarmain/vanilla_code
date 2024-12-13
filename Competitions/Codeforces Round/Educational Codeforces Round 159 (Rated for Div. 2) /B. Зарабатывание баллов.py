def main():
    n, p, le, t = map(int, input().split())
    l = 0
    r = n
    while r - l > 1:
        m = (l + r) // 2
        p0 = m * le + min(2 * m, ((n + 6) // 7)) * t
        if p0 >= p:
            r = m
        else:
            l = m
    return n - r


if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())
