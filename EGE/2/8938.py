import itertools


def f(x, y, z, w):
    f1 = (x or y)
    f2 = not y or z
    return (f1 == f2) or w


def main():
    for x1, x2, x3, x4, x5, x6, x7, x8 in itertools.product((1, 0), repeat=8):
        t = (
            (x1, 1, x2, x3),
            (x4, x5, x6, 1),
            (1, x7, x8, 1),
        )
        if len(set(t)) == 3:
            for p in itertools.permutations("xyzw", 4):
                if all(f(**dict(zip(p, l))) == 0 for l in t):
                    return "".join(p)


if __name__ == "__main__":
    print("ANS:", main())
