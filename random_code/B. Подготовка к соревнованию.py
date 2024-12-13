# https://codeforces.com/contest/158/problem/B
#
def main():
    n, k = map(int, input().split())
    m = []
    for i in range(1, n + 1):
        m.append(i)
    ans = list(reversed(m[:k+1])) + m[k+1:]
    print(*ans)

if __name__ == '__main__':
    for _ in range(int(input())):
        main()
