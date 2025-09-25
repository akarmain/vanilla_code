def game(a, b, m):
    if a == b: return m % 2 == 0
    if m == 0: return 0
    d = []
    if a > b:
        d.append(game(a, b + 1, m - 1))
        d.append(game(a, b + 3, m - 1))
    else:
        d.append(game(a + 1, b, m - 1))
        d.append(game(a + 1, b, m - 1))

    return any(d) if m % 2 != 0 else all(d)


def main():
    print("19)", min([x for x in range(1, 24) if not game(13, x, 1) and game(13, x, 2)]))
    print("22)", *[x for x in range(1, 24) if not game(13, x, 1) and game(13, x, 3)][:2])
    print("23) Иди нахуй")


if __name__ == "__main__":
    print("ANS:", main())
