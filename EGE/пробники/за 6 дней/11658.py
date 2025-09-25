"""
Откройте файл электронной таблицы, содержащей в каждой строке семь натуральных чисел. Определите наибольший номер
строки таблицы, для чисел которой выполнены оба условия:
- в строке есть одно число, которое повторяется трижды, остальные четыре числа различны;
- среднее арифметическое всех повторяющихся чисел строки больше среднего арифметического всех её чисел.
В ответе запишите только число.
"""


def main():
    n = 0
    for l in open("../../../imputs/EGE_11658.txt"):
        n+=1
        data = list(map(int, l.strip().split()))
        dub = [x for x in data if data.count(x) == 3]
        un_dub = [x for x in data if data.count(x) == 1]
        if len(set(dub)) == 1 and len(set(un_dub)) == 4:
            s_dub = sum(dub) / 3
            s_un_dub = sum(un_dub) / 4
            if s_dub > s_un_dub:
                print(n, sorted(data))


if __name__ == "__main__":
    print("ANS:", main())
