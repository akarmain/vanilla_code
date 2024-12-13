def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    k = [0] * (n + 1)
    ans = 0
    s = 0
    for i in arr:
        k[i] += 1

    for i in range(n+1):
        if k[i] >= 3:
            ans += (k[i] * (k[i] - 1) * (k[i] - 2)) // 6
        if k[i] >= 2:
            ans += (k[i] * (k[i] - 1)) // 2 * s
        s += k[i]

    return ans
if __name__ == '__main__':
    for _ in range(int(input().strip())):
        print(main())
