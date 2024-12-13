for rr in range(int(input())):
    n, m, k, H = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in a:
        if abs(i - H) % k == 0 and abs(i - H) // k < m and i != H:
            ans += 1
    print(ans)