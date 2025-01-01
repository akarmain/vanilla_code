# https://codeforces.com/contest/2043/problem/A

def main():
    n = int(input())
    ans = 1
    while n // 4 > 0:
        ans *= 2
        n //= 4
    return ans


if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())
