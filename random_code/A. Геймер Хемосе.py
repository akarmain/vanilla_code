def main():
    n, h = map(int, input().split())
    damage = list(map(int, input().split()))
    damage.sort()
    x = damage[-1]
    y = damage[-2]
    t = h % (x + y)
    m = h // (x + y)
    if t == 0:
        ans = 2 * m
    elif t <= x:
        ans = 2 * m + 1
    else:
        ans = 2 * m + 2
    return ans


if __name__ == "__main__":
    for _ in range(int(input())):
        print(main())
