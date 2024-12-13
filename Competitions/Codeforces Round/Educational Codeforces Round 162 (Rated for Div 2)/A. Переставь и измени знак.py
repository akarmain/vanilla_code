def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    f = False
    for x in a:
        if x % 3 == 1:
            f = True
    if s % 3 == 0:
        return (0)
    elif s % 3 == 2:
        return (1)
    else:
        if f:
            return (1)
        else:
            return (2)


if __name__ == '__main__':
    for _ in range(int(input())): print(main())
