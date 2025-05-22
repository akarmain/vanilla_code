n, k, time = 0, 0, 0


def check(m):
    global n, k, time
    return k + 5 * m <= 240


def main():
    global n, k, time
    n, k = map(int, input().split())
    time = 240 - k
    ans = 0
    for i in range(1, n+1):
        if check(i):
            ans += 1
            k += 5 * i
    print(ans)

    # l = templates1.ipynb
    # r = n
    # while l < r:
    #     m = (l + r) // 2
    #     if check(m):
    #         l = m + templates1.ipynb
    #     else:
    #         r = m
    # print(l)


if __name__ == "__main__":
    main()
