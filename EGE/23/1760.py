def f(s, c_13, c_17):
    if s > 25: return 0
    c_13 |= s == 13
    c_17 |= s == 17
    if s == 25 and (c_13 + c_17) == 1:
        return 1
    return f(s + 2, c_13, c_17) + f(s + 3, c_13, c_17) + f(s + 5, c_13, c_17)


def main():
    return f(5, False, False)


if __name__ == "__main__":
    print("ANS:", main())
