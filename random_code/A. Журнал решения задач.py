# https://codeforces.com/contest/158/problem/B
#
def main():
    n = int(input())
    arr = list(input())
    col = [0] * 27
    ans = 0
    for i in range(n):
        col[ord(arr[i]) - ord('A')] += 1
    for i in range(27):
        if col[i] >= i + 1:
            ans+=1
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
