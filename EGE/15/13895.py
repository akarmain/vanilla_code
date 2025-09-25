def imp(a, b):
    return not a or b


def main():
    for x in [k * 0.5 for k in range(-10000, 10000)]:
        b = 34 <= x <= 72
        c = 32 <= x <= 61
        if not (imp(b, False) and ((not c) or False)):
            print(x)
    return 72 - 32

if __name__ == "__main__":
    print("ANS:", main())
