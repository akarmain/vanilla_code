import bisect


def add(t, i, x):
    n = len(t)
    while i < n:
        t[i] += x
        i += i & -i


def get(t, i):
    s = 0
    while i > 0:
        s += t[i]
        i -= i & -i
    return s


def main():
    n = int(input())

    if n < 1 or n > 100000:
        print(-2)
        return

    h = list(map(int, input().split()))

    l = [h[i] - i - 1 for i in range(n)]
    r = [h[i] + i + 1 for i in range(n)]
    vl = sorted(set(l))
    vr = sorted(set(r))
    ml = {x: i + 1 for i, x in enumerate(vl)}
    mr = {x: i + 1 for i, x in enumerate(vr)}

    cl = [0] * (len(vl) + 1)
    sl = [0] * (len(vl) + 1)
    cr = [0] * (len(vr) + 1)
    sr = [0] * (len(vr) + 1)

    for x in r:
        p = mr[x]
        add(cr, p, 1)
        add(sr, p, x)

    suml = 0
    sumr = sum(r)
    cntl = 0
    cntr = n
    need = (n + 1) // 2
    med = None
    ans = 10 ** 30

    def count_le(x, i):
        t1 = x - i - 1
        t2 = x + i + 1
        p1 = bisect.bisect_right(vl, t1)
        p2 = bisect.bisect_right(vr, t2)
        return get(cl, p1) + get(cr, p2)

    def calc(x, i):
        t1 = x - i - 1
        t2 = x + i + 1
        p1 = bisect.bisect_right(vl, t1)
        p2 = bisect.bisect_right(vr, t2)
        c1 = get(cl, p1)
        s1 = get(sl, p1)
        c2 = get(cr, p2)
        s2 = get(sr, p2)
        res = t1 * c1 - s1 + (suml - s1) - t1 * (cntl - c1)
        res += t2 * c2 - s2 + (sumr - s2) - t2 * (cntr - c2)
        return res

    for i in range(n):
        x = l[i]
        p = ml[x]
        add(cl, p, 1)
        add(sl, p, x)
        suml += x
        cntl += 1

        x = r[i]
        p = mr[x]
        add(cr, p, -1)
        add(sr, p, -x)
        sumr -= x
        cntr -= 1

        if med is None:
            left = 0
            right = max(h) + n + 1
            while left < right:
                mid = (left + right) // 2
                if count_le(mid, i) >= need:
                    right = mid
                else:
                    left = mid + 1
            med = left
        else:
            while med > 0 and count_le(med - 1, i) >= need:
                med -= 1
            while count_le(med, i) < need:
                med += 1

        low = max(i + 1, n - i)
        cur = max(med, low)
        ans = min(ans, calc(cur, i))

    print(ans)


if __name__ == '__main__':
    main()
