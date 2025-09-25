n = 150000
k = 0
while k < 7:
    n += 1
    d = set()
    z = int(n**0.5)

    # ОЧЕНЬ ВАЖНО
    if z**2 == n:
        d.add(z)

    for i in range(2, z):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    d.discard(n)

    s = sum(d)
    if s % 13 == 10:
        print(n, s)
        k += 1
