def f(s, count_p):
    if s > 200: return 0
    if s == 200 and  count_p <= 3 : return 1
    return f(s + 2, count_p) + f(s * 3, count_p + 1) + f(s * 5, count_p + 1)


def main():
    return f(2, 0)


if __name__ == "__main__":
    print("ANS:", main())
