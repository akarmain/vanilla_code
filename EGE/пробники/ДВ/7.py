def main():
    f1 = 1920 * 1080 * 22
    f2 = 1280 * 1024 * 21
    return int(((f1 - f2) * 120) / (8 * 1024))


if __name__ == "__main__":
    print("ANS:", main())
