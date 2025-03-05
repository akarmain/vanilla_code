from itertools import product

"""
URL: https://education.yandex.ru/ege/task/1623f1e7-f1c5-4c53-8122-3a5ad8752cb2

Определите количество 12-ричных пятизначных чисел,
в записи которых ровно одна цифра 7 и не более трёх цифр с числовым значением, 
превышающим 8.
"""


def main():
    ans = 0
    for n in product('0123456789AB', repeat=5):
        n = ''.join(n)
        if n[0] == '0':
            continue
        if n.count('7') != 1:
            continue

        c = 0
        for d in n:
            if d in '9ABC':
                c += 1
        if c > 3:
            continue
        # print(n)
        ans += 1
    return ans


if __name__ == "__main__":
    print("ANS:", main())
