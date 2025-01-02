# https://codeforces.com/gym/105641/problem/1

def check(m, a, b, n):
    return abs((m - 1) * a - (n - m) * b)


def main():
    n = int(input())
    a = int(input())
    b = int(input())
    l, r = 2, n - 1
    ans = l
    min_diff = check(l, a, b, n)
    while l <= r:
        mid = (l + r) // 2
        diff = check(mid, a, b, n)

        if diff < min_diff:
            min_diff = diff
            ans = mid
        if (mid - 1) * a < (n - mid) * b:
            l = mid + 1
        else:
            r = mid - 1

    return ans


if __name__ == '__main__':
    print(main())
