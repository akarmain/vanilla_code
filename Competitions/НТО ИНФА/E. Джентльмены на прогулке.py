def main():
    d, n = map(int, input().split())
    v = list(map(int, input().split()))
    k = int(input())

    np = n * (n - 1) // 2
    ig = np

    tss = []
    td = []

    for i in range(n):
        for j in range(i + 1, n):
            v_i = v[i]
            v_j = v[j]

            T1 = 2 * d / (v_i + v_j)
            tss.append(T1)

            T2 = 2 * d / abs(v_i - v_j)
            td.append(T2)

    def F(t):
        tt = ig
        for T in tss:
            tt += int(t / T + 1e-8)
        for T in td:
            tt += int(t / T + 1e-8)
        return tt

    low = 0.0
    high = 1e15
    eps = 1e-7
    while high - low > eps:
        mid = (low + high) / 2.0
        total = F(mid)
        if total >= k:
            high = mid
        else:
            low = mid

    print("%.3f" % high)


if __name__ == '__main__':
    main()
