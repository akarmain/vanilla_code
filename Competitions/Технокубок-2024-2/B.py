def isb(w):
    m = len(w)
    for i in range(m // 2):
        if w[i] == w[m - i - 1]:
            return True
    return False


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        n = len(s)
        if n < 2:
            print(-1)
            continue
        if isb(s):
            print(0)
            continue
        from collections import Counter
        cnt = Counter(s)
        if all(c == 1 for c in cnt.values()):
            print(-1)
            continue
        mbb = False
        for i in range(n):
            new_s = s[:i] + s[i + 1:]
            if len(new_s) >= 2 and isb(new_s):
                print(1)
                mbb = True
                break

        if mbb:
            continue
        print(n - 2)


if __name__ == '__main__':
    main()
