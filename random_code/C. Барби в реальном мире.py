def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print("YES" if sum(a)%m==0 else "NO")


if __name__ == '__main__':
    main()
