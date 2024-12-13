def f(arr, index):
    arr = arr[:]
    arr[index] += 1
    c = 1
    for j in arr:
        c *= j
    return c


def main():
    ans = []
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        c = f(arr, i)
        ans.append(c)
    return max(ans)


if __name__ == '__main__':
    for i in range(int(input())):
        print(main())
