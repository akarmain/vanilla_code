def main():
    n, k, l, p = map(int, input().split())
    cpb = 2 * k
    b_min = (n + cpb - 1) // cpb

    if b_min == 1:
        return -1

    tbl = b_min * 2 * p
    max_d = (l - tbl) // (b_min - 1)

    if max_d < 0:
        return -1
    else:
        return max_d


if __name__ == "__main__":
    print(main())
