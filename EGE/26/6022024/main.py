def main():
    f = open('26.txt', 'r')
    n = int(f.readline())
    arr = []
    for line in f:
        arr.append(list(map(int, line.split())))
    arr.sort()
    f = []
    s = []
    ans = 0
    wind_1 = 0
    for t1, t2, wind in arr:
        while len(f) > 0 and f[0] <= t1:
            f.pop(0)
            wind_1 += 1
        while len(s) > 0 and s[0] <= t1:
            s.pop(0)

        if wind == 1 or (wind == 0 and (len(f) <= len(s))):
            if len(f) == 0:
                f.append(t1 + t2)
            elif len(f) < 12:
                f.append(f[-1] + t2)
            else:
                ans += 1
        else:
            if len(s) == 0:
                s.append(t1 + t2)
            elif len(s) < 12:
                s.append(s[-1] + t2)
            else:
                ans += 1


    print(f)
    print(s)
    print(wind_1+len(f), ans)


if __name__ == '__main__':
    main()
