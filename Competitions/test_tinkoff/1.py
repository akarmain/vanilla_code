def main():
    n, m =  map(int, input().split())
    i0 = 0
    a0 = -1000000
    for i in range(n):
        i, a = map(int, input().split())
        if a > a0:
            a0 = a
            i0 = i

    j0 = 0
    b0 = -1000000
    for _ in range(m):
        j, b = map(int, input().split())
        if b > b0:
            b0 = b
            j0 = j
    print(i0, j0)

"""
2 3
1 234
2 23423
1 23
5 234
7 23432
"""

if __name__ == '__main__':
    main()
