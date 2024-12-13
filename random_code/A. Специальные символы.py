def main():
        n = int(input())
        if n % 2 == 1:
            print("NO")
        else:
            print("YES")
            for i in range(n // 2):
                for j in range(2):
                    print("AB"[i % 2], end='')
            print()

if __name__ == "__main__":
    for i in range(int(input())):
        main()