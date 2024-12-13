def main():
    n, m = map(int, input().split())
    x = input()
    s = input()
    for i in range(6):
        if s in x:
            print(i)
            return
        x += x
    print(-1)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
