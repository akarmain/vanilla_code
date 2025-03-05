p = int(input())
r = int(input())
m = int(input())

if p * r / 100 > m * 12:
    print("False")
    print(0)
else:
    d = p
    i = 0
    t = 0
    while d > 0 and t < 600:
        if t % 12 == 0:
            i += d * r / 100
        if m >= i:
            d -= (m - i)
            i = 0
        else:
            i -= m
        t += 1
    if d <= 0:
        print("True")
        print(t)
    else:
        print("False")
        print(0)