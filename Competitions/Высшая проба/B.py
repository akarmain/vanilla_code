def main():
    n, k, p = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    t = sum(c)
    l, r = 0, t
    while l < r:
        m = (l + r) // 2
        if m + m // k >= t:
            r = m
        else:
            l = m + 1
    m = l
    f_items = t - m
    fr, pd = [], []
    for pr, q in zip(a, c):
        if pr <= p:
            fr.append((pr, q))
        else:
            pd.append((pr, q))
    fr.sort(reverse=True)
    pd += [(pr, q) for pr, q in zip(a, c) if pr <= p]
    pd.sort()
    fr_sel, rem = [], f_items
    for pr, q in fr:
        take = min(q, rem)
        fr_sel.append((pr, take))
        rem -= take
        if rem == 0:
            break
    pd_res = []
    for pr, q in pd:
        f_q = 0
        for fp, fq in fr_sel:
            if fp == pr:
                f_q = fq
                break
        rem_q = q - f_q
        if rem_q > 0:
            pd_res.append((pr, rem_q))
    paid, cost = 0, 0
    for pr, q in pd_res:
        if paid >= m:
            break
        take = min(q, m - paid)
        cost += pr * take
        paid += take
    print(cost)


if __name__ == "__main__":
    main()
