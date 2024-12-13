n, m = map(int, input().split())
ini = [input().strip() for _ in range(m)]
input()
fin = [input().strip() for _ in range(m - 1)]

from collections import Counter

ic, fc = [Counter() for _ in range(n)], [Counter() for _ in range(n)]
for d in ini:
    for i, nt in enumerate(d):
        ic[i][nt] += 1
for d in fin:
    for i, nt in enumerate(d):
        fc[i][nt] += 1

res, nts = '', 'ACGT'
for i in range(n):
    for nt in nts:
        if ic[i].get(nt, 0) - fc[i].get(nt, 0) == 1:
            res += nt
            break

print(res)
