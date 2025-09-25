"""
Сколько существует шестнадцатеричных четырёхзначных чисел,
содержащих в своей записи ровно одну цифру 9, в которых
никакие две чётные или две нечётные цифры не стоят рядом?
"""

from itertools import product


def main():
    ans = 0
    for w in product("0123456789ABCDEF", repeat=4):
        if w.count("9") == 1 and w[0] != "0" :
            w = "".join(w)
            w = w.replace("0", "c")
            w = w.replace("2", "c")
            w = w.replace("4", "c")
            w = w.replace("6", "c")
            w = w.replace("8", "c")
            w = w.replace("A", "c")
            w = w.replace("C", "c")
            w = w.replace("E", "c")


            w = w.replace("1", "n")
            w = w.replace("3", "n")
            w = w.replace("5", "n")
            w = w.replace("7", "n")
            w = w.replace("9", "n")
            w = w.replace("B", "n")
            w = w.replace("D", "n")
            w = w.replace("F", "n")
            if "cncn" == w or "ncnc" == w:
                ans += 1
    return ans


if __name__ == "__main__":
    print("ANS:", main())
