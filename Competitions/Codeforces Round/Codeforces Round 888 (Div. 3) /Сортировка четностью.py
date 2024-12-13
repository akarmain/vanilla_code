for rr in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = a[:]
    b.sort()
    f = True
    for i in range(n):
        if a[i] % 2 != b[i] % 2:
            f = False
    if f:
        print("YES")
    else:
        print("NO")