def main():
    s = input()
    for i in range(1, 9):
        s1 = s[0] + str(i)
        if s1 != s:
            print(s1)
    for i in range(ord('a'), ord('h') + 1):
        s1 = chr(i) + s[1]
        if s1 != s:
            print(s1)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
