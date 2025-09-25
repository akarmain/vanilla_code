def game(s1, s2, m):
    if s1 + s2 >= 65: return m % 2 == 0
    if m == 0: return 0
    h = [game(s1 + 1, s2, m - 1),
         game(s1, s2 + 1, m - 1),
         game(s1 * 3, s2, m - 1),
         game(s1, s2 * 3, m - 1)]
    return any(h) if m % 2 != 0 else all(h)


def main():
    # print("19)", min([s for s in range(1, 59) if game(6, s, 2)]))
    print(7)
    print("20)", [s for s in range(1, 59) if not game(6, s, 1) and game(6, s, 3)])
    print("21)", min([s for s in range(1, 59) if (game(6, s, 2) or game(6, s, 4)) and not game(6, s, 2)]))
    ...


if __name__ == "__main__":
    print("ANS:", main())
