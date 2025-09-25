def f(s, c_9, c_14):
    if s > 18: return 0
    if s == 18 and c_9 and not c_14: return 1
    c_9 |= s == 9
    c_14 |= s == 14
    return f(s + 1, c_9, c_14) + f(s + 3, c_9, c_14)


def main():
    return f(2, False, False)


if __name__ == "__main__":
    print("ANS:", main())
