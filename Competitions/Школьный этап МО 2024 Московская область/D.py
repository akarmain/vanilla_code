def count_black(x1, y1, x2, y2):
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    if area % 2 == 0:
        return area // 2
    else:
        if (x1 + y1) % 2 == 0:
            return area // 2 + 1
        else:
            return area // 2


def main():
    n, m = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())

    ta = n * m
    tg = count_black(1, 1, n, m)
    tw = ta - tg
    eb = count_black(x1, y1, x2, y2)
    ea = (x2 - x1 + 1) * (y2 - y1 + 1)
    ew = ea - eb
    return min(tg - eb, tw - ew)


if __name__ == "__main__":
    print(main())
