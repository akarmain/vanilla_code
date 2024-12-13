def main():
    s = input()
    ans = 0
    n = len(s)
    for k in range(n//2, 0, -1):
        cnt = 0
        for i in range(n-k):
            j = i+k
            if s[i] == s[j] or s[i] == '?' or s[j] == '?':
                cnt += 1
            else:
                cnt = 0

            if cnt == k:
                ans = max(ans, cnt * 2)
    return ans

if __name__ == "__main__":
    for i in range(int(input())):
        print(main())
