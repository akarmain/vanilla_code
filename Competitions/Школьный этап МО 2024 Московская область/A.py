def main():
    n, m = map(int, input().split())
    all_clep = n * m

    if n % 2 == 0 and m % 2 == 0:
        clet_rm = 4
    elif n % 2 == 0 or m % 2 == 0:
        clet_rm = 2
    else:
        clet_rm = 1
    return all_clep - clet_rm


if __name__ == '__main__':
    print(main())
