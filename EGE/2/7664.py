def f(a, b, d, c):
    f1 = ((a and b) == (not c))
    # f2 = (b and d)
    # f2 = (b == d)
    f2 = ((not b) or d)
    # f2 = (b or d)
    return f1 and f2


def main():
    p = (
        (1, 0, 0, 0, 1),
        (1, 0, 1, 0, 1),
        (1, 0, 1, 1, 1),
        (1, 1, 0, 0, 1),
    )
    return all(f(**dict(zip("cadb", l))) == 1 for l in p)


if __name__ == "__main__":
    print("IS ANS:", main())
