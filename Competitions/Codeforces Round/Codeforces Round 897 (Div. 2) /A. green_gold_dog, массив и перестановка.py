def main() -> None:
    n = int(input())
    arr = list(map(int, input().split()))
    list_c = []
    for i in range(n):
        for j in range(0, -n - 1, -1):  # 0, -n - 1, -1
            c = arr[i] - j
            if not c in list_c:
                print(c, end=' ')
                break


if __name__ == '__main__':
    for i in range(int(input())):
        main()
        print()

