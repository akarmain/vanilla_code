n = int(input())
b = []
for _ in range(n):
    s = input()
    a, c = s.split('-')
    h1, m1 = map(int, a.split(':'))
    h2, m2 = map(int, c.split(':'))
    b.append((h1 * 60 + m1, h2 * 60 + m2))
b.sort()
d = []
p = 600
for s, e in b:
    if p < s:
        d.append((p, s))
    p = max(p, e)
if p < 1140:
    d.append((p, 1140))
t = 0
m = 600
for s, e in d:
    c = max(s, m)
    while c < e:
        x = min(c + 20, e)
        t += x - c
        m = x + 10
        c = m
print(t)
