"""
Ученица составляет 5-буквенные слова из букв ГЕПАРД.
При этом в каждом слове ровно одна буква Г, слово не может начинаться на букву А
и заканчиваться буквой Е. Какое количество слов может составить ученица?
"""
from itertools import product


def main():
    ans = 0

    for w in list(product('ГЕПАРД', repeat=5)):
        if w.count('Г') == 1 and w[0] != 'А' and w[-1] != 'Е':
            ans += 1

    return ans


if __name__ == "__main__":
    print("ANS:", main())
