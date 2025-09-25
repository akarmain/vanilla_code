"""
Сколько существует восьмеричных пятизначных чисел, не содержащих в своей записи цифру 1, в которых все
цифры различны и

    никакие две чётные или две нечётные цифры не стоят рядом?
"""
from itertools import permutations


def main():
    ans = 0
    for d in permutations("0234567", r=5):
        d = "".join(d)
        d = d.replace("0", "c")
        d = d.replace("2", "c")
        d = d.replace("3", "n")
        d = d.replace("4", "c")
        d = d.replace("5", "n")
        d = d.replace("6", "c")
        d = d.replace("7", "n")
        if not ("cc" in d or "nn" in d):
            ans += 1
    return ans


if __name__ == "__main__":
    print("ANS:", main())
