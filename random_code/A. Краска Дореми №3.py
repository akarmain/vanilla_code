def main():
    n = int(input())
    arr = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[arr[i]] = 0

    for i in range(n):
        d[arr[i]] += 1

if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())
