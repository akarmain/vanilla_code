"""
Определите количество пятизначных чисел, записанных в восьмеричной системе счисления, в записи которых только одна цифра б, при этом
никакая нечётная цифра не стоит рядом с цифрой 6.
"""

from itertools import product, count

def main():
    ans = 0
    for d in product("01234567", repeat=5):
        if d[0] == "0":
            continue
        if d.count("6") != 1:
            continue

        d = "".join(d)
        d = d.replace("1", "n")
        d = d.replace("3", "n")
        d = d.replace("5", "n")
        d = d.replace("7", "n")
        if "n6" in d or "6n" in d or "n6n" in d :
            continue
        print(d)


        ans += 1
    return ans

if __name__ == "__main__":
    print("ANS:", main())
