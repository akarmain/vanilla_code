def main():
    n = int(input())
    ans = 0
    while n > 0:
        ans += n
        n //= 2
    return ans


if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())
