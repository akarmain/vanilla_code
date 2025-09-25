"""
Определите количество строк в электронной таблице, каждая из которых содержит четыре натуральных числа и соответствует только одному из следующих критериев:
– В строке нет повторяющихся чисел,
    а целая часть среднего арифметического максимального и минимального чисел присутствует в строке.
– В строке есть повторяющиеся числа, и сумма квадратов этих чисел меньше суммы квадратов неповторяющихся чисел.
Подсчитайте количество строк, удовлетворяющих только одному из этих условий, и укажите результат в ответе.
"""


def sum_sqr(l: list):
    ans = 0
    for d in l:
        ans += d ** 2
    return ans


def main():
    ans = 0
    f = open("../../imputs/EGE_7335.csv")
    for line in f:
        data = list(map(int, line.strip().split(";")))

        if len(data) == len(set(data)):
            if data.count(int((max(data) + min(data)) / 2)) == 1:
                ans += 1
        else:
            pov = []
            ne_pov = []
            for d in data:
                if data.count(d) == 1:
                    pov.append(d)
                else:
                    ne_pov.append(d)
            if sum_sqr(ne_pov) < sum_sqr(pov):
                ans += 1

    return ans


if __name__ == "__main__":
    print("ANS:", main())
