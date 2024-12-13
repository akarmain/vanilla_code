def main():
    n = int(input())
    for i in range(1, n + 1, 2):
        j = i
        while j <= n:
            print(j, end=" ")
            j *= 2


if __name__ == "__main__":
    for i in range(int(input())):
        main()
        print()
