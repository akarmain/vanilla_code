def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[-1] == arr[0]:
        print("-templates1.ipynb")
        return

    it = 0
    while arr[it] == arr[0]:
        it += 1
    print(it, n - it)
    for j in range(it):
        print(arr[j], end=" ")
    for j in range(it, n):
        print(arr[j], end=" ")


if __name__ == "__main__":
    for _ in range(int(input())):
        main()
