def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 99999
    c = 0
    for i in range(n):
        if arr[i] % 2 == 0:
            c += 1
        if arr[i] % k == 0:
            return 0
        ans = min(ans, k - arr[i] % k)
    if k != 4:
        return ans
    else:
        return min(max(2 - c, 0), ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())
