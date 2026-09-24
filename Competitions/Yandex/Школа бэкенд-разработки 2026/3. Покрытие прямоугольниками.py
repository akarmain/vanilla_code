def main():
    n = int(input())

    if n < 1 or n > 5000:
        print(-2)
        return

    a = []

    for _ in range(n):
        x, y = map(int, input().split())
        if x == 0 or y == 0 or abs(x) > 50000000 or abs(y) > 50000000:
            print(-2)
            return
        a.append((abs(x), abs(y)))

    a.sort()
    b = []
    mx = 0

    for x, y in reversed(a):
        if y > mx:
            b.append((x, y))
            mx = y

    b.reverse()
    m = len(b)
    dp = [0] + [10 ** 40] * m

    for i in range(1, m + 1):
        x = b[i - 1][0]
        best = 10 ** 40
        for j in range(1, i + 1):
            cur = dp[j - 1] + x * b[j - 1][1]
            if cur < best:
                best = cur
        dp[i] = best

    print(dp[m] * 4)


if __name__ == '__main__':
    main()
