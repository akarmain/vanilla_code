def main():
    n, k = map(int, input().split())
    v = [int(input()) for _ in range(n)]
    tr = 0
    cs = 1
    for i in range(k):
        ds = v[i % n]
        rn = (ds - cs + n) % n
        tr += rn
        cs = ds
    print(tr)


if __name__ == "__main__":
    main()
