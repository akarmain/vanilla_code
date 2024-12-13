def main():
    n = int(input())
    arr = list(map(int, input().split()))
    ma = max(arr)
    mi = min(arr)
    c_max = arr.count(ma)
    c_min = arr.count(mi)
    if ma == mi:
        return 0, int(((n - 1) / 2) * n)
    return ma - mi, c_max * c_min


if __name__ == '__main__':
    print(*main())
