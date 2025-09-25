def f(s, c_12):
    if s > 25: return 0
    if s == 25 and c_12: return 1
    c_12 |= s == 12

    return f(s + 2, c_12) + f(s + 3, c_12) + f((s * 10) + 1, c_12)


def main():
    return f(3, False)


if __name__ == "__main__":
    print("ANS:", main())
