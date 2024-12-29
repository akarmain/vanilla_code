def main():
    l, k, u, m = map(int, input().split())
    n = int(input())
    obs = []
    for _ in range(n):
        p, h = map(int, input().split())
        obs.append([p, h])
    d = int(input())
    dr = []
    for _ in range(d):
        dr.append(int(input()))
    obs.sort(key=lambda x: x[0])
    dr.sort()
    c = 0
    if not obs:
        while c < l:
            c += m
            if c >= l: print(l);return

    def shoot(pos):
        s = u
        for o in obs:
            if o[1] > 0 and pos < o[0] <= pos + k:
                if any(pos < dd < o[0] for dd in dr): continue
                r = min(o[1], s)
                o[1] -= r
                s -= r
                if not s: break

    while True:
        shoot(c)
        np = c + m
        for o in obs:
            if o[1] > 0 and c < o[0] <= np:
                print(o[0])
                return
        c = np
        if c >= l:
            print(l)
            return


if __name__ == "__main__":
    main()
