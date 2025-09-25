def main():
    t = 31 * 60 + 62
    s = 18_324_531
    f1 = 2 * 41_000 * 8 * t
    f2 = 1 * 4_000 * 56 * t
    return (f1 - f2) / s



if __name__ == "__main__":
    print("ANS:", main())
