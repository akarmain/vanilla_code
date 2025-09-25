def game(s1, s2, m):
    if s1 + s2 >= 342: return m % 2 == 0
    if m == 0: return 0
    h = [game(s1 + 2, s2, m - 1),
         game(s1, s2 + 2, m - 1),
         game(s1, s2 * 5, m - 1),
         game(s1 * 5, s2, m - 1)]
    return any(h) if m % 2 != 0 else all(h)


def main():
    print("19)", 14)
    print("20)", [s for s in range(1, 326) if not game(11, s, 1) and game(11, s, 3)])
    print("21)", *[s for s in range(1, 326) if game(11, s, 4) and not game(11, s, 2)])
    ...


if __name__ == "__main__":
    main()
