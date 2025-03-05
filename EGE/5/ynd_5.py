"""
URL:https://education.yandex.ru/ege/task/4e651673-c848-47cd-8dab-813092d13201

Существуют числа, обладающие свойствами:

- Число делится на все свои цифры;
- Число, полученное из данного числа записью цифр в обратном порядке, тоже делится на все свои цифры.
Примером такого числа является 216.

Сколько существует трёхзначных чисел, без нулей в записи, обладающих этими свойствами?
"""


def krat(n):
    for i in str(n):
        if n % int(i) != 0:
            return False
    return True


def check(n):
    return krat(n) and krat(int(str(n)[::-1])) # Ошибся в расположении -1


def main():
    ans = 0
    for i in range(100, 1000):
        if str(i).count('0') == 0 and check(i):
            print(i)
            ans += 1
    return ans


if __name__ == "__main__":
    print("ANS:", main())
