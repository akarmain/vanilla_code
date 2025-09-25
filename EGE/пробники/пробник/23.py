"""
URL: https://education.yandex.ru/ege/task/c0707fa0-019f-4c29-815b-16b1d678b30e
GPT
"""


def f(x, y):
    if x > y or x == 16:
        return 0
    if x == y:
        return 1
    return f(x + 2, y) + f(x + 3, y) + f(x ** 2, y)


def main():
    return f(2, 25) * f(25, 42)


if __name__ == "__main__":
    print("ANS:", main())
