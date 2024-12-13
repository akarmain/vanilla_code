def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[n-1]-arr[0]+arr[-1]-arr[n])
    for i in range(n):
        print(arr[i], arr[n+i])


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
