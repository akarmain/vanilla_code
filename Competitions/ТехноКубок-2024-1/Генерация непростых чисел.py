def count_valid_numbers_revised(n):
    MOD = 998244353

    # Однозначные числа - только 5 подходит
    if n == 1:
        return 1

    # Для чисел длиной больше 1
    total = 0

    # Для всех длин чисел кроме последней цифры
    for length in range(1, n):
        # Выбираем любую цифру кроме 0 и кратной 3 на первое место
        first_digit_options = 8  # {1, 2, 4, 5, 7, 8, 9}
        # Остальные цифры могут быть любыми, кроме того, что одна из них должна быть нечетной
        other_digits_options = 9 * pow(10, length - 2, MOD) # 9 вариантов на каждую позицию, кроме последней

        # Умножаем варианты для первой и остальных цифр
        total += first_digit_options * other_digits_options

    # Добавляем варианты для последней цифры
    # Последняя цифра должна быть четной (0, 2, 4, 6, 8), но не 0 если n = 2
    last_digit_options = 5 if n > 2 else 4
    total += last_digit_options * pow(10, n - 2, MOD)

    return total % MOD

print(count_valid_numbers_revised(1))  # Пример 1
print(count_valid_numbers_revised(2))  # Пример 2

