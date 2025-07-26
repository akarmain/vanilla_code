def rec(start, stop, k):
    if start > stop:
        return 0
    if start == stop or k >= 5:
        return 1
    return rec(start + 1, stop, k) + rec(start * 3, stop, k + 1) + rec(start * 4, stop, k + 1)


print(rec(3, 300, 0))
# 200
# 200
