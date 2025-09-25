def game(k, m):
    if k < 273: return m % 2 == 0
    if m == 0: return 0
    h = [game(k + 2, m - 1), game(k + 5, m - 1), game(k * 4, m - 1)]
    # return any(h) if m % 2 != 0 else any(h)  # меняем all на any в 19 задаче
    return any(h) if m%2!=0 else any(h) # меняем all на any в 19 задаче


def main():

    print("19)", min(s for s in range(1, 273) if game(s, 2)))
    print("20)", [i for i in range(1, 273) if game(i, 3)])
    print("21)", [i for i in range(1, 273) if game(i, 2)])
    ...


if __name__ == "__main__":
    main()
