import itertools


def f(x, y, z, w):
    f1 = (not (y and (x == (not z))) or w)
    f2 = (not z or y)

    return f1 and f2


def main():
    for x1, x2, x3, x4, x5 in itertools.product([0, 1], repeat=5):
        t = (
            (0, 0, x1, x2, 0),
            (0, x3, 0, 0, 0),
            (1, x4, x5, 1, 0)
        )
        if len(t) == len(set(t)):
            for p in itertools.permutations("xyzw", 4):
                if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                    print("".join(p))


if __name__ == "__main__":
    print("ANS:", main())
