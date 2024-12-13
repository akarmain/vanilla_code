

def main():
    a = int(input())
    b = []
    for _ in range(a):
        c = input().split()
        d = c[0]
        e = int(c[1])
        b.append((e, d))
    f = sorted(b, key=lambda x: -x[0])
    g = sorted(b, key=lambda x: x[0])
    h = (a + 1) // 2
    i = a - h
    j = f[:h]
    k = g[:i]
    l = 0
    m = 0
    n = []
    for o in range(1, a + 1):
        if o % 2 == 1:
            n.append(j[l][1])
            l += 1
        else:
            n.append(k[m][1])
            m += 1
    return ' '.join(n)


if __name__ == "__main__":
    print(main())
