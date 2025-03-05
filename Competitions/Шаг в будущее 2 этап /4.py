X = int(input())
Y = int(input())
b = [list(map(int, input().split()))]

r = [30, 30, 30, 30]
m = 0
bd = [[] for _ in range(4)]

while m < 100:
    m += 1
    if m % 10 == 0:
        for i in range(4):
            r[i] += X

    for i in range(4):
        for j in range(5):
            if b[i][j] == m:
                c = [[8, 3, 10, 0], [5, 0, 8, 0], [10, 6, 10, 0], [8, 4, 8, 0]][i]
                t = [5, 5, 10, 8][i]
                if all(r[k] >= c[k] for k in range(4)):
                    for k in range(4):
                        r[k] -= c[k]
                    bd[i].append([m + t - 1, m + t])

    for i in range(4):
        for x in bd[i]:
            if m > x[0]:
                if i == 0 and m % 2 == x[1] % 2:
                    r[0] += 2
                    r[2] += 5
                    if (m - x[0]) % 5 == 0:
                        r[0] -= 3
                    x[1] += 2
                elif i == 1 and (m - x[0]) % 5 == 0:
                    r[3] += 7
                    if (m - x[0]) % 10 == 0:
                        r[2] -= 2
                    x[1] += 5
                elif i == 2 and (m - x[0]) % 10 == 0:
                    r[1] += 6
                    if (m - x[0]) % 18 == 0:
                        r[0] -= 2
                    x[1] += 10
                elif i == 3 and (m - x[0]) % 8 == 0:
                    r[2] += 8
                    if (m - x[0]) % 12 == 0:
                        r[0] -= 1
                        r[1] -= 1
                    x[1] += 8

    for i in range(4):
        r[i] -= Y
        if r[i] <= 0:
            print(m)
            for x in r:
                print(x)
            exit()

print(100)
for x in r:
    print(x)