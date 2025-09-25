from itertools import permutations, product


def f(x, y, z, w):
    return (x and (not y)) or (x == z) or w


def main():
    for x1, x2, x3, x4 in product((1, 0), repeat=4):
        t = (
            (x1, x2, 0, 1),
            (1, 0, x3, 1),
                (1, 1, 0, x4),
        )
        if len(set(t)) == 3:
            for p in permutations("xyzw", r=4):
                if all(f(**dict(zip(p, l))) == 0 for l in t):
                    print(*p)


if __name__ == "__main__":
    print("ANS:", main())
