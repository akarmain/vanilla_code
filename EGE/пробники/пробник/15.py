"""
URL: https://education.yandex.ru/ege/task/ee49ebf0-8990-49b7-8d0e-e64660ae9a65

"""


def algos(i):
    p = list(range(64, 95 + 1))
    q = list(range(72, 106 + 1))
    return not ((i in p) and (i not in q) or (not (i not in p) or (i not in q)))


def main():
    ans = 0
    for i in range(3, 10001):
        if algos(i):
            ans += 1
    return ans


if __name__ == "__main__":
    print("ANS:", main())
