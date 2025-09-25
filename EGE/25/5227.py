import re


def div(x):
    divs = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.add(i)
            divs.add(x // i)
    return sorted(list(divs))


def main():
    for d in range(10 ** 7):
        if re.fullmatch(r"3\d*52\d", str(d)):
            if len(div(d)) % 2 != 0:
                print(d, div(d)[-2])
    ...


if __name__ == "__main__":
    print(div(3143529))
    print("ANS:", main())
"""
3 \d* 52  \d"

3 143  52 9
"""