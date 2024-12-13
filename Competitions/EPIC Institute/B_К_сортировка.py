def main():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [arr[0]]
    for i in range(n - 1):
        ans.append(max(ans[i], arr[i + 1]))
    for i in range(n):
        ans[i] = ans[i] - arr[i]
    return sum(ans)+max(ans)

    # s = 0
    # ans.sort()
    # for i in range(n-1):
    #     s += (ans[i + 1] - ans[i]) * (n - i)
    #
    # return s


if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())
