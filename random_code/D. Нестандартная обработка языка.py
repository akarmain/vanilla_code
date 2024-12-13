def main():
    n = int(input())
    s = input() + "!"
    print(s[0], end="")
    for i in range(1, n):
        if s[i+1] in "ae":
            print(".", end="")
        print(s[i],end="")
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        main()
