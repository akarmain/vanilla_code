"""
Определите количество шестизначных чисел, записанных в семеричной системе счисления,
которые не оканчиваются на цифры, меньшие 4,
а также содержат поровну четных и нечетных цифр.

"""
from itertools import product


def main():
    ans = 0
    for d in product("0123456", repeat=6):
        if d[0] == "0":
            continue

        if int(d[-1]) < 4:
            continue

        even = d.count("0") + d.count("2") + d.count("4") + d.count("6")
        odd = d.count("1") + d.count("3") + d.count("5")
        if even != odd:
            continue

        ans += 1
    return ans

if __name__ == "__main__":
    print("ANS:", main())
