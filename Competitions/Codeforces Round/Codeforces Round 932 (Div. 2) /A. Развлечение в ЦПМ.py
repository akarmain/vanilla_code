def main():
    n = int(input())
    s = input()
    return min(s[::-1]+s, s)


if __name__ == '__main__':
    for i in range(int(input())):
        print(main())
