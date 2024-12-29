def main():
    n, m, k = map(int, input().split())
    p = 3
    fld = []
    for _ in range(n):
        fld.append(list(map(int, input().split())))
        p += m
    x = int(input())
    p += 1
    dct = {}
    for _ in range(x):
        a, b, c_ = input().split(";")
        a, b, c_ = int(a), int(b), int(c_)
        dct[(b - 1, c_ - 1)] = a
        p += 1
    v = set()
    r = n - 1
    c = k - 1
    s = 0
    d = 1
    mv = {1: (-1, 0), 2: (0, 1), 3: (1, 0), 4: (0, -1)}
    while True:
        if r < 0 or r >= n or c < 0 or c >= m:
            print(0)
            print(s)
            return
        if (r, c) in v:
            print(r + 1, c + 1)
            print(s)
            return
        v.add((r, c))
        s += fld[r][c]
        if (r, c) in dct:
            d = dct[(r, c)]
        rr, cc = mv[d]
        r += rr
        c += cc


if __name__ == "__main__":
    main()
