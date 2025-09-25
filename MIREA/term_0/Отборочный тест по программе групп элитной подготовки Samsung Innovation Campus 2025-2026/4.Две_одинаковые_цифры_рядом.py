s = input().strip()
print('YES' if any(a == b for a, b in zip(s, s[1:])) else 'NO')
