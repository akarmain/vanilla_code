from itertools import permutations, product


def f(x, y, z, w, u):
    f1 = (not z) or w
    f2 = y == (not x)
    f3 = y or z
    return (not (f1 and f2)) or (u == f3)


def main():
    for x1, x2, x3, x4, x5, x6, x7, x8 in product((1, 0), repeat=8):
        p = (
            (0, x1, 0, 0, 0),
            (0, x2, x3, 0, 0),
            (x5, 0, 0, 0, x4),
            (0, 0, x6, x7, x8),
        )
        if len(set(p)) == 4:
            for t in permutations("xyzwu", r=5):
                if all(f(**dict(zip(t, l))) == 0 for l in p):
                    return "".join(t)


if __name__ == "__main__":
    print("ANS:", main())
