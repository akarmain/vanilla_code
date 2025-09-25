def main():
    f = [0] * 3000
    for n in range(3000):
        if n <= 3:
            f[n] = 1
        if n > 3:
            f[n] = (n + 3) * f[n - 2]
    return f[2028] / f[2024]


if __name__ == "__main__":
    print("ANS: ", main())
