def t2m(t): return int(t[:2]) * 60 + int(t[3:])


n = int(input())
sp = []
for i in range(n):
    c = int(input())
    for _ in range(c):
        s, e = input().split('-')
        sp.append((i, t2m(s), t2m(e)))
sp.sort(key=lambda x: x[1])
need = (n + 1) // 2

INF = 10 ** 9
T = len(sp)
dp = [[(INF, -1)] * (need + 1) for _ in range(T)]
for i in range(T):
    dp[i][1] = (0, -1)


def w(i, j):
    return max(0, (sp[j][1] + 5) - (sp[i][2] - 5))


for i in range(T):
    for k in range(1, need):
        if dp[i][k][0] == INF:
            continue
        for j in range(i + 1, T):
            if sp[i][0] != sp[j][0]:
                nw = dp[i][k][0] + w(i, j)
                if nw < dp[j][k + 1][0]:
                    dp[j][k + 1] = (nw, i)
best = (INF, -1)
for i in range(T):
    w_i = dp[i][need][0]
    if w_i < best[0]:
        best = (w_i, i)
res = []
cur = best[1]
k = need
while cur != -1:
    res.append(cur)
    cur = dp[cur][k][1]
    k -= 1
res = res[::-1]
times = [(sp[i][1], sp[i][2]) for i in res]
lcc, wait = 0, 0
cur_start, cur_end = times[0]
for s, e in times[1:]:
    gap = max(0, s - cur_end)
    wait += gap
    cur_end = e
lcc = cur_end - cur_start

print(f"{cur_start // 60:02d}:{cur_start % 60:02d}")
print(lcc)
print(wait)
