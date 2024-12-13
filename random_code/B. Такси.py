# https://codeforces.com/contest/158/problem/B
#
def main():
    n = input()
    arr = list(map(int, input().split()))
    a1 = arr.count(1)
    a2 = arr.count(2)
    a3 = arr.count(3)
    a4 = arr.count(4)
    ans = a4 + a3
    a1 = max(0, a1 - a3)
    ans += (a2 * 2 + a1 + 3) // 4
    print(ans)


if __name__ == '__main__':
    main()
