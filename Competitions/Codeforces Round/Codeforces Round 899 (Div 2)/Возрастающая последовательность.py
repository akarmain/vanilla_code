def main():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = arr[:]
    for i in range(n):
        if ans[i] == arr[i]:
            c = ans[-1]
            ans.append(c + 1)
        else:
            ans.append(arr[i])

    print(*ans[1:])


if __name__ == '__main__':
    for i in range(int(input())):
        main()
