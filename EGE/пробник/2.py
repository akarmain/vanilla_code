"""
URL: https://education.yandex.ru/ege/task/c84e2709-a311-49ae-9a1d-7279bb7cf568

w∧(y≡(z→(x∨y)))
"""


def main():
    print("x y z w")
    for x in (0, 1):
        for y in (0, 1):
            for z in (0, 1):
                for w in (0, 1):
                    if w and (y == (not z or (x or y))):
                        print(x, y, z, w)


if __name__ == "__main__":
    main()
