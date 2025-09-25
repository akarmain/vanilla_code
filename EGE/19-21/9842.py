def game(s, m):
    if s >= 111: return m % 2 == 0
    if m == 0: return 0
    d = [game(s + 3, m - 1), game(s + 1, m - 1), game(s * 4, m - 1)]
    return any(d) if m % 2 != 0 else all(d)


def main():
    print("19", [s for s in range(1, 111) if not game(s, 1) and game(s, 2)])
    print("20", [s for s in range(1, 111) if (not game(s, 1)) and (game(s, 3))])
    print("21", [s for s in range(1, 111) if not game(s, 2) and (game(s, 4) )])


if __name__ == "__main__":
    print("ANS:", main())
