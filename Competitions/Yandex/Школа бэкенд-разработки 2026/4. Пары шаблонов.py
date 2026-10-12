def main():
    data = open(0, 'rb').read().split()
    n = int(data[0])
    m = int(data[1])

    if n < 1 or n > 50000 or m < 1 or m > 6:
        print(-2)
        return

    size = 1 << m
    bit = [0] * size
    sub = [[] for _ in range(size)]

    for mask in range(size):
        for i in range(m):
            if mask >> i & 1:
                bit[mask] |= 31 << (i * 5)

        x = mask

        while True:
            sub[mask].append(x)

            if x == 0:
                break

            x = (x - 1) & mask

    arr = [{} for _ in range(size)]

    for s in data[2:2 + n]:
        mask = 0
        code = 0

        for i, c in enumerate(s):
            if c != 63:
                mask |= 1 << i
                code |= (c - 96) << (i * 5)

        arr[mask][code] = arr[mask].get(code, 0) + 1

    proj = [[None] * size for _ in range(size)]

    for mask in range(size):
        if not arr[mask]:
            continue

        items = list(arr[mask].items())

        for cur in sub[mask]:
            d = {}
            b = bit[cur]

            for code, cnt in items:
                key = code & b
                d[key] = d.get(key, 0) + cnt

            proj[mask][cur] = d

    ans = 0

    for a in range(size):
        if not arr[a]:
            continue

        ca = sum(arr[a].values())

        for b in range(a, size):
            if not arr[b]:
                continue

            cur = a & b
            x = proj[a][cur]
            y = proj[b][cur]

            if len(x) > len(y):
                x, y = y, x

            cnt = 0

            for key, val in x.items():
                cnt += val * y.get(key, 0)

            if a == b:
                ans += (cnt - ca) // 2
            else:
                ans += cnt

    print(ans)


if __name__ == '__main__':
    main()
