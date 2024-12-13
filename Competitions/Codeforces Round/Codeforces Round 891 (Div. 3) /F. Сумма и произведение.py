for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    l = []
    for g in range(k):
        x, y = list(map(int, input().split()))
        for i in range(n):
            for j in range(i + 1, n):
                print(f"a[i] + a[j] == x ({a[i] + a[j] == x})\n"
                      f"a[i] * a[j] == x ({a[i] * a[j] == y})")
    print(a, n)
