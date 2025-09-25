"""
(М. Ишимов) Сколько существует шестеричных семизначных чисел, содержащих в своей записи ровно одну цифру 2,
при этом никакая чётная цифра не стоит рядом с цифрой 2?
"""

from itertools import product


def main():
    ans = 0
    for d in product("012345", repeat=7):
        if d[0] == "0":
            continue
        if d.count("2") != 1:
            continue

        d = "".join(d)
        d = d.replace("0", "c")
        d = d.replace("4", "c")

        if "2c" in d or "c2" in d:
            continue
        ans += 1
    return ans


if __name__ == "__main__":
    print("ANS:", main())
