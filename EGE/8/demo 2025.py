from itertools import product
p = product('0123456789ABC', repeat = 5)
# print(list(p)[-1])
ans = 0
for s in p:
    if s[0] != '0' and (s.count('7') == 1) and (s.count('9') + s.count('A') + s.count('B') + s.count('C') <= 3):
        ans += 1
print(ans)
