def game(s, m):
    if s <= 87: return m % 2 == 0
    if m == 0: return 0
    d = [
        game(s - 2, m - 1),
        game(s // 2, m - 1),
    ]
    return any(d) if m % 2 != 0 else all(d)


def main():
    print("19)", [x for x in range(89, 10000) if not game(x, 1) and game(x, 2)])
    ...


if __name__ == "__main__":
    print("ANS:", main())
