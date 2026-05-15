def count_divisors(n: int) -> int:
    cnt = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            cnt += 1
            if i != n // i:
                cnt += 1
        i += 1
    return cnt


result = []
for x in range(999_999_999, 100_000_000, -1):
    d = count_divisors(x)
    if d < x and (x - d) % 17 == 0:
        result.append(x)
    if len(result) == 5:
        break
print(*sorted(result))
