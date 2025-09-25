"""
Сколько существует восьмеричных пятизначных чисел,

не содержащих в своей записи цифру 1, в которых все цифры различны и никакие
две чётные или две нечётные цифры не стоят рядом?
"""
from itertools import permutations


def main():
    ans = 0
    for d in permutations("01234567", r=5):
        if d[0] == "0" or d.count("1") >= 1:
            continue


        d = "".join(d)
        d = d.replace("0", "c")
        d = d.replace("2", "c")
        d = d.replace("4", "c")
        d = d.replace("6", "c")

        d = d.replace("1", "n")
        d = d.replace("3", "n")
        d = d.replace("5", "n")
        d = d.replace("7", "n")

        if d == "cncnc" or d == "ncncn":
            ans += 1

    return ans


if __name__ == "__main__":
    print("ANS:", main())
