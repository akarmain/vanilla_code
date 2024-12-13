def main():
    n, l = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = max(arr[0], l-arr[n-1])
    for i in range(n - 1):
        ans = max(ans, (arr[i + 1] - arr[i])/2)
    print(ans)


if __name__ == "__main__":
    main()
