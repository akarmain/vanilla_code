def game(k, m):
    if m >= 55: return m % 2 == 0
    if m == 0: return 0
    d = [game(k + 1, m - 1), game(k + 4, m - 1), game(k * 4, m - 1)]
    return any(d) if m % 2 != 0 else any(d)


def main():
    print("19)", [s for s in range(1, 55) if not game(s, 1) and game(s, 2)])
    # print("20)", [s for s in range(1, 55)] if game())
    # print("21)", [s for s in range(1, 55)] if game())
    ...

