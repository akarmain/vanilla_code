"""
URL:https://education.yandex.ru/ege/task/d1b752f8-587f-47c2-8187-7975a7684715
GROK-3-Think
"""


def main():
    # Считываем строку из файла
    with open("../../imputs/EGE_24_ya_пробник_0.txt", "r") as f:
        S = f.readline().strip()

    # Разделяем строку по '+' на произведения
    P = S.split('+')
    # Создаем список: True, если в произведении есть "0", иначе False
    B = ["0" in p.split('*') for p in P]

    max_length = 0
    i = 0
    # Проходим по списку B
    while i < len(P):
        if B[i]:
            j = i
            current_sum = len(P[i])  # Длина текущего произведения
            # Расширяем последовательность, пока следующее произведение содержит "0"
            while j + 1 < len(P) and B[j + 1]:
                j += 1
                current_sum += 1 + len(P[j])  # Добавляем '+' и следующее произведение
            max_length = max(max_length, current_sum)
            i = j + 1
        else:
            i += 1

    print(max_length)


if __name__ == "__main__":
    main()
