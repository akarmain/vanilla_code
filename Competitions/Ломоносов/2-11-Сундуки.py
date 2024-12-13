def many(s):
    ans = 0
    i0 = 0
    a = [1, 5, 10, 50, 100, 200, 500, 1000, 2500]
    A = [500, 1000, 5000, 10_000, 20_000, 50_000, 100_000, 200_000, 500_000]
    for i in range(len(s)):
        if ord('a') <= ord(s[i]) <= ord('z'):
            ans += int(s[i0:i]) * a[ord(s[i]) - 97]
            i0 = i + 1
        if ord('A') < ord(s[i]) <= ord('Z'):
            ans += int(s[i0:i]) * A[ord(s[i]) - 65]
            i0 = i + 1
    return ans


def main():
    n = int(input())
    a = []
    for i in range(n):
        x = many(input())
        a.append(x)
        print(x)
    i_max = 0
    j_max = 0
    j1 = 0
    for i in range(1, n):
        if a[i - 1] <= a[j1]:
            j1 = i - 1
        if a[i] - a[j1] >= a[i_max] - a[j_max] and i+j1 > i_max+j_max:
            i_max = i
            j_max = j1
    print(j_max+1)
    print(i_max+1)

if __name__ == '__main__':
    main()
