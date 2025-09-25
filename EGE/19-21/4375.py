def game(k, m, last=None):
    if k >= 29: return m % 2 == 0
    if m == 0: return 0
    if last == "+1":
        d = [
            game(k + 2, m - 1, "+2"),
            game(k * 2, m - 1, "*2"),
        ]
    elif last == "+2":
        d = [
            game(k + 1, m - 1, "+1"),
            game(k * 2, m - 1, "*2"),
        ]
    elif last == "*2":
        d = [
            game(k + 1, m - 1, "+1"),
            game(k + 2, m - 1, "+2"),
        ]
    else:
        d = [
            game(k + 1, m - 1, "+1"),
            game(k + 2, m - 1, "+2"),
            game(k * 2, m - 1, "*2"),
        ]

    return any(d) if m % 2 != 0 else all(d)


def main():
    print("19", min([x for x in range(1, 29) if not game(x, 1) and game(x, 3)]))
    ...


if __name__ == "__main__":
    print("ANS:", main())
