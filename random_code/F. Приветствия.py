def binary_search(b, x):
    r = len(b)
    l = 0
    while r - l > 1:
        m = (l + r) // 2
        if b[m] > x:
            r = m - 1
        else:
            l = m
    if x == b[l]:
        return l
    return r


def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append([x, y])
        b.append(y)

    a.sort()
    b.sort()
    ans = 0
    for i in range(n):
        k = binary_search(b, a[i][1])
        ans += k
        b = b[:k] + b[k + 1:]
    print(ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        main()


"""
15	0
15	0
2	1; 2
5	3
12	3
11	5
12	4; 6
12	7
13	0
10	0
4	9
13	10
7	0
14	13
"""