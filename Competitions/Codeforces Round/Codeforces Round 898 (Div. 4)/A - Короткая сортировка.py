def main():
    s = input()
    if s[0] == 'a' or s[1] == 'b' or s[2] == 'c':
        return "YES"
    return "NO"


if __name__ == '__main__':
    for i in range(int(input())):
        print(main())