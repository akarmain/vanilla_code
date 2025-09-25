import itertools


def f(a, b, t, c):
    f1 = ((not a) or b)
    f2 = (c >= (not a))
    f3 = (t and (not a) or c and (not b))
    return f1 and f2 and f3


def main():
    t = (
        (1, 0, 0, 1, 0),
        (1, 1, 0, 1, 1),
        (0, 0, 0, 1, 0),
        (1, 0, 0, 0, 1),
    )
    for p in itertools.permutations("abct", r=4):
        if all(f(**dict(zip(p, l))) == l[-1] for l in t):
            print(*p)

if __name__ == "__main__":
    print("ANS:", main())
