def main():
    n, m, k = map(int, input().split())
    dx = n - 1
    dy = m - 1
    mn = min(dx, dy)
    df = max(dx, dy) - mn
    t1 = (df + k - 1) // k
    t2 = (mn + k - 1) // k
    print(t1 + t2)

if __name__ == '__main__':
    main()