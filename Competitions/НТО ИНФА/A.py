def get(a, b):
    return min(a, b)


def main():
    ai, bi = map(int, input().split())
    ci, di = map(int, input().split())

    if ai * bi > ci * di:
        a, b = min(ai, bi), max(bi, ai)
        c, d = min(di, ci), max(di, ci)
    else:
        a, b = min(di, ci), max(di, ci)
        c, d = min(ai, bi), max(bi, ai)
    r1 = get(a + c, min(b, d))
    r2 = get(a + d, min(b, c))
    r3 = get(min(a, c), a + d)
    r4 = get(min(a, d), b + c)
    ans = [min(a, b), min(c, d), r1, r2, r3, r4]
    return max(ans)


if __name__ == '__main__':
    print(main())
