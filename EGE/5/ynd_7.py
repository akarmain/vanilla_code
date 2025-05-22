"""
URL: https://education.yandex.ru/ege/task/638ac2c9-defe-4ca9-971a-ee65a1774d31
"""


def algos(n: int) -> int:
    """Преобразует число N по заданному алгоритму и возвращает R"""
    # Переводим число в троичную систему
    n_3 = ''
    while n > 0:
        n_3 = str(n % 3) + n_3
        n //= 3  # Деление нацело на 3

    # Проверяем сумму цифр в троичной записи
    if sum(map(int, n_3)) % 2 == 0:
        n_3 += "0"  # Дописываем "0" справа
        result_str = "2" + n_3[2:]  # Заменяем два первых разряда на "2"
    else:
        n_3 += "templates1.ipynb"  # Дописываем "templates1.ipynb" справа
        result_str = "20" + n_3[2:]  # Заменяем два первых разряда на "20"

    # Переводим обратно в десятичную систему
    return int(result_str, 3)


def main():
    best_n = None
    best_R = None
    for i in range(1, 200):
        R = algos(i)
        if R > 75:
            if best_R is None or R < best_R:
                best_R = R
                best_n = i
    return best_n

if __name__ == "__main__":
    print("ANS:", main())  # Вывод: 44
