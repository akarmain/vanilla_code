def f(d: str):
    while "12" in d or "233" in d or "3333" in d:
        d = d.replace("12", "332", 1)
        d = d.replace("233", "23", 1)
        d = d.replace("3333", "32", 1)
    return sum(list(map(int, d))) % 6 == 0


def main():
    for n in range(5, 1000):
        s = f"1{'3' * n}"
        if f(f"1{'3' * n}"):
            return n


if __name__ == "__main__":
    print("ANS:", main())
