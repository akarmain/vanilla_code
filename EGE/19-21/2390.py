def game(s, m):
    if 50 <= s <= 119: return m % 2 == 0
    if s > 119: return m % 2 != 0
    if m == 0: return 0

    d = [
        game(s + 2, m - 1),
        game(s * 3, m - 1),
    ]
    return any(d) if m % 2 != 0 else all(d)


def main():
    print("19)", len([s for s in range(1, 50) if game(s, 2)]))
    print("20)", [s for s in range(1, 50) if not game(s, 1) and game(s, 3)])
    print("21)", [s for s in range(1, 50) if not game(s, 2) and game(s, 4)])


if __name__ == "__main__":
    print("ANS:", main())
