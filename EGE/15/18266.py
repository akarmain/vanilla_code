def imp(a, b):
    return not a or b


def main():
    for a in range(1, 10000):
        f = True
        for x in range(1, 10000):
            cond1 = (x & 57) == 0
            cond2 = imp((x & 23) == 0, not ((x & a) == 0))
            if not (cond1 or cond2):
                f = False
        if f:
            return a


if __name__ == "__main__":
    print("ANS:", main())
