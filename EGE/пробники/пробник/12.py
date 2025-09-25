"""
URL: https://education.yandex.ru/ege/task/eacee230-7f5b-42b1-98a1-93fa5ba5d996

"""
import sys

sys.set_int_max_str_digits(999999999)


def algos(n):
    s = '0' + "2" * n
    while "002" in s or "22" in s:
        if "002" in s:
            s = s.replace("002", "44", 1)
        else:
            s = s.replace("22", "0", 1)
        if "222" in s:
            s = s.replace("222", "2", 1)
    return sum(map(int, s))


def main():
    ans = []
    for i in range(3, 10000):
        if algos(i) == 42:
            print(i)
            ans.append(i)
    return ans


if __name__ == "__main__":
    print(algos(5))
    print("ANS:", main())
