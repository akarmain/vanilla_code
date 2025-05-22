def main():
    n = int(input())
    a = list(map(int, input().split()))
    pr = [0] * n
    for i in range(n):
        if a[i] == a[i - 1]:
            pr[i] = pr[i - 1]
        else:
            pr[i] = i
    for _ in range(int(input())):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        if pr[l] == pr[r]:
            print('-templates1.ipynb -templates1.ipynb')
        else:
            print(pr[r], r + 1)
    print()


if __name__ == "__main__":
    for _ in range(int(input())):
        main()
