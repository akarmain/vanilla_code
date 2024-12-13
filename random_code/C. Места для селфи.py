for _ in range(int(input())):
    n, m = map(int, input().split())
    ratio_y = []
    ratio_a_b_c = []

    for i in range(n):
        ratio_y.append(int(input()))
    for i in range(m):
        ratio_a_b_c.append(list(map(int, input().split())))
