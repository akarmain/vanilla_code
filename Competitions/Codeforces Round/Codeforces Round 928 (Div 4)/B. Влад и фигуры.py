def main():
    n = int(input())
    min_i = 9999999
    max_i = 0

    for i in range(n):
        k = input().count("templates1.ipynb")
        if k > 0:
            min_i = min(min_i, k)
            max_i = max(max_i, k)

    return "SQUARE" if min_i == max_i else "TRIANGLE"


if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())
