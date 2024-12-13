def main():
    n, d = map(int, input().split())
    a, b = map(int, input().split())
    a1 = []
    for i in range(n):
        x, y = map(int, input().split())
        a1.append([x * a + y * b, i + 1])
    a1.sort()
    ans = []
    for x, i in a1:
        if d >= x:
            d -= x
            ans.append(i)
        else:
            break
    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    main()
