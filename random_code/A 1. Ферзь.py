def main():
    n = int(input())
    m = int(input())
    ans = n - 1 + m - 1 + 2 * (min(n, m) - 1)
    if n % 2 == 0 and m % 2 == 0 and n == m:
        ans -= 1
    print(ans)


if __name__ == '__main__':
    main()
