import sys
from functools import lru_cache

# Увеличиваем лимит рекурсии на случай глубоких вложений (хотя для 52 это не критично)
sys.setrecursionlimit(2000)

@lru_cache(None)
def count_programs(current_num, has_16, has_24):
    """
    current_num: текущее число на экране
    has_16: булевый флаг, посещали ли мы число 16
    has_24: булевый флаг, посещали ли мы число 24
    """

    # 1. Проверка ограничений (запрещенные числа и выход за границы)
    if current_num > 52 or current_num == 31 or current_num == 45:
        return 0

    # 2. Обновление состояния флагов
    if current_num == 16:
        has_16 = True
    if current_num == 24:
        has_24 = True

    # 3. Базовый случай: достигли целевого числа
    if current_num == 52:
        # Условие: траектория содержит 16 ИЛИ 24
        if has_16 or has_24:
            return 1
        else:
            return 0

    # 4. Рекурсивный шаг: суммируем результаты всех возможных команд
    # Команда A: +2
    # Команда B: +3
    # Команда C: *2
    return (count_programs(current_num + 2, has_16, has_24) +
            count_programs(current_num + 3, has_16, has_24) +
            count_programs(current_num * 2, has_16, has_24))

# Вызов функции для начального числа 10 с исходными флагами False
result = count_programs(10, False, False)

print(result)
