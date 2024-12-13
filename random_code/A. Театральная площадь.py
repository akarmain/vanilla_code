from math import ceil

def main():
    n, m, a = map(int, input().split())
    print(ceil(n / a) * ceil(m / a))


if __name__ == "__main__":
    main()
