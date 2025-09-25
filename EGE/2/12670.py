from itertools import product, permutations


def f(x, y, z, w):
    f1 = x and (not y)
    f2 = (z and w)
    f3 = (not y) or z
    f4 = (not w) or x
    return ((not f1) or f2) and (f3 or f4)


def main():
    for x1, x2, x3, x4, x5, x6 in product((0, 1), repeat=6):
        t = (
            (x1, x2, 1, 1),
            (1, x3, 1, x4),
            (x5, 0, x6, 1),
        )
        if len(set(t)) == 3:
            for p in permutations("xyzw", 4):
                if all(f(**dict(zip(p, l))) == 0 for l in t):
                    return "".join(p)


if __name__ == "__main__":
    print("ANS:", main())
