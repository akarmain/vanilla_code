import math

def solve(d, l, r):
    divs = []
    for i in range(1, int(math.sqrt(d)) + 1):
        if d % i == 0:
            divs.append(i)
            if i != d // i:
                divs.append(d // i)
    count = 0
    for a in divs:
        if a >= math.sqrt(d):
            break
        b = d // a
        if a < b and (a % 2 == b % 2):
            x = (a + b) / 2
            y = (b - a) / 2
            y2 = y * y
            x2 = x * x
            if l <= y2 < x2 <= r:
                count += 1
    return count

d, l, r = map(int, input().split())
print(solve(d, l, r))