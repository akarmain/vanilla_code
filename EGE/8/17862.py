"""
Определите количество 12-ричных пятизначных чисел, в записи которых ровно одна
цифра 7 и не более трёх цифр с числовым значением, превышающим 8.
"""
from itertools import product


def main():
    ans = 0
    for p in product("0123456789AB", repeat=5):
        if p[0] == "0":
            continue

        if p.count("7") != 1:
            continue

        if sum([p.count("9"), p.count("A"), p.count("B")]) > 3:
            continue

        ans += 1
    return ans


if __name__ == "__main__":
    print("ANS:", main())
