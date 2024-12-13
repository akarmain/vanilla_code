def main():
    s, n = map(int, input().split())
    a = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append([x, y])
    a.sort()
    f = True
    for x, y in a:
        if s > x:
            s+=y
        else:
            f = False
            break
    if f:
        print('YES')
    else:
        print('NO')
if __name__ == '__main__':
    main()
