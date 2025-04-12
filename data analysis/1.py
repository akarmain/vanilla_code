import os
import string
from pprint import pprint


def main():
    data = {}
    gp = "/Users/akarmain/PycharmProjects/vanilla_code/imputs/elements/"
    lf = os.listdir(gp)
    for file in lf:
        f = open(gp + file)
        for l in f.readlines():
            l = l.lower()
            l =l.replace('\n', '')
            l =l.replace(',', '')
            l =l.replace('(', '')
            l =l.replace(')', '')

            for word in l.split():
                try:
                    data[word] += 1
                except:
                    data[word] = 1
    # Сортируем по убыванию частоты
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
    # Берём первые три
    return sorted_data[:3]

if __name__ == "__main__":
    pprint(main())
