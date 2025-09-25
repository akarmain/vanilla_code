def diz(a, b):
    return not a or b


def main():
    for x in [k * 0.25 for k in range(-10000, 10000)]:
        a = 0
        p = 5 <= x <= 280
        q = 295 <= x <= 400
        r = 375 <= x <= 450
        if (diz(q, p) or diz(not a, r)) != 1:
            print(x)
    return 80


if __name__ == "__main__":
    print("ANS:", main())
