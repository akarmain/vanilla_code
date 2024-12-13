for i_ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        if a[i]%k>0:
            a[i] %= k
        else:
            a[i] = k
    for i in range(n):
        maix = a.index(max(a))
        a[maix] = 0
        print(maix + 1, end=" ")
    print()

for rr in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = []

    for i in range(n):
        if a[i] % k > 0:
            b.append([a[i] % k, i]) else:
            b.append([k, i])
        b.sort(reverse=True)
        for x in b:
            print(x[1] + 1, end=
            " ")