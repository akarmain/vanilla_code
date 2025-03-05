"""
URL: https://education.yandex.ru/ege/task/525fcbaa-ca74-4f79-af9c-90a644e1cfc1
GPT-o3-mini
"""


def main():
    data = []
    with open("../../imputs/EGE_17_ya_пробник.txt", "r", encoding="utf-8") as f:
        for line in f:
            data.append(int(line.strip()))

    # 1. Ищем максимум среди чисел, оканчивающихся на 18 (по модулю).
    candidates = [x for x in data if abs(x) % 100 == 18]
    if not candidates:
        # Если нет ни одного числа, оканчивающегося на 18, то условие «сумма ≤ …» невыполнимо
        return "0 0"
    max_ends18 = max(candidates)

    # Функция проверки «содержит ли число цифру '3'»
    def has_digit_3(x):
        return '3' in str(abs(x))

    count_valid = 0  # Счётчик подходящих троек
    max_sum_valid = None  # Максимальная сумма среди подходящих троек

    # 2. Перебираем все тройки подряд идущих элементов
    for i in range(len(data) - 2):
        triple = data[i], data[i + 1], data[i + 2]

        # Условие «не более двух из трёх содержат '3'»
        count_3 = sum(has_digit_3(x) for x in triple)
        if count_3 <= 2:
            s = sum(triple)
            # Условие «сумма ≤ max_ends18»
            if s <= max_ends18:
                count_valid += 1
                if max_sum_valid is None or s > max_sum_valid:
                    max_sum_valid = s

    # Если подходящих троек не найдено, выводим «0 0»
    if count_valid == 0:
        return "0 0"
    else:
        return f"{count_valid} {max_sum_valid}"


if __name__ == "__main__":
    answer = main()
    print("ANS:", answer)
