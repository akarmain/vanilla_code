def f(s, count_c):
    if s > 64: return 0
    if s == 64 and count_c == 8: return 1
    return f(s + 2, count_c + 1) + f(s + 4, count_c + 1) + f(s * 2, count_c + 1)


def main():
    return f(4, 0)


if __name__ == "__main__":
    print("ANS:", main())
