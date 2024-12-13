import bisect as bic
for _ in range(int(input())):
    n, m = map(int, input().split())
    k = [0]
    for i in range(n):
        c, t = map(int, input().split())
        k.append(c*t+k[-1])
    # print(k)
    lm = list(map(int, input().split()))
    for i in m:
        print()
        # print(bic.bisect_right(k, m))
    # l = len(b)
