from collections import deque


n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
vd = [False] * (n + 1)

def cq(N_c):
    if N_c == 0:
        return (0, 0, 0)
    ng_3 = N_c // 3
    r = N_c % 3
    if r == 0:
        ns = 0
        np = 0
    elif r == 1:
        if ng_3 >= 1:
            ng_3 -= 1
            np = 2
            ns = 0
        else:
            ns = 1
            np = 0
    elif r == 2:
        np = 1
        ns = 0
    return (ns, np, ng_3)


ts = 0
tp = 0
tg = 0

for i in range(1, n+1):
    if not vd[i]:
        qqq = deque()
        qqq.append(i)
        vd[i] = True
        css = 1
        while qqq:
            u = qqq.popleft()
            for v in adj[u]:
                if not vd[v]:
                    vd[v] = True
                    css += 1
                    qqq.append(v)
        ns, nnpp, nuu = cq(css)
        ts += ns
        tp += nnpp
        tg += nuu

print(ts)
print(tp)
print(tg)
