"""
В файле электронной таблицы в каждой строке записаны шесть натуральных чисел. Определите количество строк таблицы, для которых
выполнены оба условия:
– в строке только одно число повторяется 4 раза;
– квадрат числа, которое повторяется 4 раза, меньше суммы оставшихся чисел строки.
В ответе запишите только число.
"""


def main():
    ans = 0
    for l in open('../../imputs/EGE_19228.txt', 'r'):
        data = list(map(int, l.strip().split("	")))
        vals4 = [d for d in set(data) if data.count(d) == 4]
        if len(vals4) == 1:
            x = vals4[0]
            others = [d for d in data if d != x]
            if x * x < sum(others):
                ans += 1
    return ans


if __name__ == "__main__":
    print("ANS:", main())
