def main():
    n, a, b = map(int, input().split())
    print(min(n*a, n//2*b+(n%2)*a))


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
