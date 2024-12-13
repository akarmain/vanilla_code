def main():
    n = int(input())
    x = input()
    y = input()
    ans = 0
    if x != y:
        for i in range(1, n + 1):
            if len(str(i)) == str(i).count(x) + str(i).count(y):
                ans += 1
    else:
        for i in range(1, n + 1):
            if len(str(i)) == str(i).count(x):
                ans += 1
    if ans == 0:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
