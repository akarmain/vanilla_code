import re


def div(n):
    res = {1, n}
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            res |= {k, n // k}
    return res


def main():
    for n in range(10 ** 6):
        c = re.compile(r"4\d*")
        d = div(n)
        mask_divs = [x for x in d if c.fullmatch(str(x))]
        if len(mask_divs) == 24:
            return (n, max(mask_divs))


if __name__ == "__main__":
    print("ANS:", main())
