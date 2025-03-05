def calculate_distance(phone_number, direction):
    # Словарь с координатами цифр на циферблате
    keypad = {
        '1': (0, 0), '2': (1, 0), '3': (2, 0),
        '4': (0, 1), '5': (1, 1), '6': (2, 1),
        '7': (0, 2), '8': (1, 2), '9': (2, 2),
        '0': (1, 3)
    }

    # Переменная для хранения общего расстояния
    total_distance = 0

    # Проходим по всем цифрам в телефоне, начиная с второй
    for i in range(1, len(phone_number)):
        current_digit = phone_number[i - 1]
        next_digit = phone_number[i]

        # Получаем координаты текущей и следующей цифры
        x1, y1 = keypad[current_digit]
        x2, y2 = keypad[next_digit]

        # Вычисляем расстояние по указанному направлению
        if direction == 0:  # горизонтально
            total_distance += abs(x2 - x1)
        elif direction == 1:  # вертикально
            total_distance += abs(y2 - y1)

    return total_distance


# Ввод данных
phone_number = input().strip()
direction = int(input().strip())

# Вывод результата
print(calculate_distance(phone_number, direction))