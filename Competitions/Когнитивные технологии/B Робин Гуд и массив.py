def main():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(n - 1):
        ans = max(ans, min(arr[i], arr[i + 1]))
    return ans


if __name__ == '__main__':
    print(main())
