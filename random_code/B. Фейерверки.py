def main():
    a, b, m = map(int, input().split())
    return 2+m//a + m//b

if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())