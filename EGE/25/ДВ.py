def is_p(d):
    ans = set()
    for i in range(0, int(d ** 0.5) + 1):
        if d % 2 == 0:
            ans.add(d)
            ans.add(d // i)
    return list(ans) == 0


def dev(d):
    ans = set()
    for i in range(2, int(d ** 0.5) + 1):
        if d % 2 == 0:
            ans.add(d)
            ans.add(d // i)
    return list(ans)


def main():
    for d in range(2_750_000, 3_170_000):
        ds = dev(d)
        if ds == 2:
            x1 = ds[0]
            x2 = ds[1]
            if is_p(x1) and is_p(x2):
                print(d, x1, x2)


if __name__ == "__main__":
    print(is_p(7))
    print(is_p(10))
    print(is_p(4))
    print("ANS:", main())
