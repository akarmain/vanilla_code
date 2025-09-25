from itertools import permutations


def f(x, y, z):
    return (not z) and x or x and y


def main():
    t = (
        (0, 0, 0, 0),
        (0, 0, 1, 1),
        (0, 1, 0, 0),
        (0, 1, 1, 1),
        (1, 0, 0, 0),
        (1, 1, 1, 1),
    )
    for p in permutations("xyz", r=3):
        if all(f(**dict(zip(p, l))) == l[-1] for l in t):
            print("".join(p))


if __name__ == "__main__":
    print("ANS:", main())
