def con(a, b):
    return not a or b


def main():
    for x in [k * 0.25 for k in range(-10000, 10001)]:
        p = 35 <= x <= 55
        q = 45 <= x <= 65
        if (con(p, 0) and con(1, not q)) != 1:
            print(x)


if __name__ == "__main__":
    print("ANS:", main())
