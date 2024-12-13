def main():
    a, b = map(int, input().split())
    f = lambda x, y, c: (c-a) + (b-c)
    print(f(a, b, 1))
    l = 0
    r = 200


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
