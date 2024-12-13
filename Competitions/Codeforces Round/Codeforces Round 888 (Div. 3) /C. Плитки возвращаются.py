for rr in range(int(input())):
    f = True
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    left = 0
    right = 0
    i = 0
    j = n - 1
    k_left = k
    k_right = k

    if c[0] == c[n - 1]:
        k_left = k // 2
        k_right = k - k_left

    while i < n and left < k_left:
        if c[i] == c[0]:
            left += 1
        i += 1

    while j >= 0 and right < k_right:
        if c[j] == c[n - 1]:
            right += 1
        j -= 1

    print("YES" if (i - 1) < (j + 1) else "NO")
