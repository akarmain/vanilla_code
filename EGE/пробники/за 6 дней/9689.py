from itertools import permutations, product


def f(x, y, w, z):
    f1 = (w or x or y)
    f2 = (y or z)
    f3 = (w or z)
    b = (f2 and x or y and f3)
    return (not f1) or b


def main():
    for x1, x2, x3, x4, x5 in product((1, 0), repeat=5):
        t = (
            (0, 0, 0, x1),
            (x2, 1, 1, x3),
            (x4, 1, x5, 1),
        )
        if len(set(t)) == 3:
            for p in permutations("xyzw", r=4):
                if all(f(**dict(zip(p, l))) == 0 for l in t):
                    return "".join(p)


if __name__ == "__main__":
    print("ANS:", main())
