def main():
    t = int(input().strip())
    d = list(input().strip())
    n = t
    sd = sum(map(int, d))
    if sd % 3 != 0:
        print(-1)
        return

    ep = [i for i, d in enumerate(d) if int(d) % 2 == 0]
    if not ep:
        print(-1)
        return

    if int(d[-1]) % 2 == 0:
        print(0)
        return

    bc = None
    for i in ep:
        cost = (n - 1 - i)
        if i == 0 and n > 1 and d[1] == '0':
            continue
        if bc is None or cost < bc:
            bc = cost

    print(bc if bc is not None else -1)



if __name__ == '__main__':
    main()
