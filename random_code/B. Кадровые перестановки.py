def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = float('inf')
    a = [0] + a + [0]
    s_pref = [0] * (n + 2)
    s_pr = 0
    for i in range(1, n + 1):
        s_pr += a[i]
        s_pref[i] = s_pref[i - 1] + s_pr
    s_suff = [0] * (n + 2)
    s_su = 0
    for i in range(n, 0, -1):
        s_su += a[i]
        s_suff[i] = s_suff[i + 1] + s_su
    for i in range(1, n + 1):
        s1 = s_pref[i - 1] + s_suff[i + 1]
        s = min(s, s1)
    print(s)


if __name__ == '__main__':
    main()
