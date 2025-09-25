"""
Сколько существует шестнадцатеричных трёхзначных чисел,
в которых все цифры различны и никакие две чётные или две нечётные цифры
не стоят рядом?
"""
from itertools import permutations


def main():
    ans = 0
    for d in permutations("0123456789ABCDEF", r=3):
        if d[0] == "0":
            continue

        d = "".join(d)
        d = d.replace("0", "c")
        d = d.replace("1", "n")
        d = d.replace("2", "c")
        d = d.replace("3", "n")
        d = d.replace("4", "c")
        d = d.replace("5", "n")
        d = d.replace("6", "c")
        d = d.replace("7", "n")
        d = d.replace("8", "c")
        d = d.replace("9", "n")

        d = d.replace("A", "c")
        d = d.replace("B", "n")
        d = d.replace("C", "c")
        d = d.replace("D", "n")
        d = d.replace("E", "c")
        d = d.replace("F", "n")

        if d == "cnc" or d == "ncn":
            ans += 1

    return ans


if __name__ == "__main__":
    print("ANS:", main())
