def main():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    s1 = 0
    cnt = 0
    for i in range(n):
        if s1 + a[i] <= s:
            cnt += 1
            s1 += a[i]
        else:
            break
    if cnt < n and s1 + a[cnt] - a[cnt // 2] <= s:
        cnt += 1
    if cnt == 0:
        cnt = 1
    print(cnt)

if __name__ == '__main__':
    main()
