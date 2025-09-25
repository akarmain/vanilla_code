def imp(a, b):
    return not a or b


def main():
    a = 1
    ff = 1
    for x in [k * 0.25 for k in range(-10000, 10000)]:
        p = 6 <= x <= 17
        q = 13 <= x <= 28
        f = imp(a, p) or q
        if f == ff:
            print(x)
    return 22

if __name__ == "__main__":
    print("ANS:", main())
