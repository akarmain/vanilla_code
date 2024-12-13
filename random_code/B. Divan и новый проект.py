def main():
    n = int(input())
    x = input().split()
    a = []
    i = 0
    for y in x:
        a.append([int(y), i])
        i += 1
    a.sort(reverse=True)
    t = 0
    ans = [0] * n
    i0 = 2
    for x, i in a:
        t += x * (i0 // 2)
        if i0 % 2 != 0:
            ans[i] = i0 // 2
        else:
            ans[i] = -i0 // 2
        i0 += 1
    print(2 * t)
    print(0, end=' ')
    print(*ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
