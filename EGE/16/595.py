def f(n):
    if n <= 3:
        return n
    if 3 < n <= 32:
        return n // 4 + f(n - 3)
    if n > 32:
        return 2 * f(n - 5)


def main():
    return f(100)


if __name__ == "__main__":
    print("ANS:", main())
