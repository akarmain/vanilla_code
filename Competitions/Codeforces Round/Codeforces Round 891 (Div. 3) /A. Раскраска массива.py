

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cc = 0
    nn = 0
    for i in range(n):
        if a[i] % 2 == 0:
            cc += a[i]
        else:
            nn += a[i]
    # print(cc, nn, sum(a))
    if (cc + nn) % 2 == 0 and sum(a) % 2 == 0:
        print("YES")
    else:
        print("NO")
