"""
URL: https://education.yandex.ru/ege/task/ee49ebf0-8990-49b7-8d0e-e64660ae9a65

"""


def main():
    # Функция переводит число из системы с основанием 22 в десятичное значение.
    def from_base22(s, x_val, y_val):
        # Заменяем символы переменных x и y на их числовые значения
        s = s.replace('x', str(x_val)).replace('y', str(y_val))
        value = 0
        for ch in s:
            # Если символ — цифра, то его значение:
            # (так как все цифры записаны в десятичном виде, и все числа меньше 10 уже корректны)
            digit = int(ch)
            value = value * 22 + digit
        return value

    # Альтернативный способ: вычисляем значение выражения напрямую по формуле,
    # где x и y выступают как переменные.
    # Число 34256x4 (в основе 22) представлено цифрами:
    # 3 * 22^6 + 4 * 22^5 + 2 * 22^4 + 5 * 22^3 + 6 * 22^2 + x * 22^templates1.ipynb + 4 * 22^0.
    # Число 72847y3 (в основе 22):
    # 7 * 22^6 + 2 * 22^5 + 8 * 22^4 + 4 * 22^3 + 7 * 22^2 + y * 22^templates1.ipynb + 3 * 22^0.
    # Сумма S = N1 + N2 = A + 22*(x + y), где A — константа:
    # A = (3+7)*22^6 + (4+2)*22^5 + (2+8)*22^4 + (5+4)*22^3 + (6+7)*22^2 + (4+3)
    # Вычислим A:
    p22 = [1]
    for i in range(1, 7):
        p22.append(p22[-1] * 22)
    # p22[i] = 22^i; p22[6] = 22^6.
    A = (3 + 7) * p22[6] + (4 + 2) * p22[5] + (2 + 8) * p22[4] + (5 + 4) * p22[3] + (6 + 7) * p22[2] + (4 + 3)
    # Вычислим p22:
    # 22^2 = 484, 22^3 = 10648, 22^4 = 234256, 22^5 = 5153632, 22^6 = 113379904.
    # Таким образом, A = 10*113379904 + 6*5153632 + 10*234256 + 9*10648 + 13*484 + 7.
    # Посчитаем A:
    # 10*113379904 = 1133799040
    # 6*5153632   = 30921792
    # 10*234256   = 2342560
    # 9*10648     = 95832
    # 13*484      = 6292
    # A = 1133799040 + 30921792 + 2342560 + 95832 + 6292 + 7 = 1167165523
    # Таким образом, S = 1167165523 + 22*(x+y)

    A = 1167165523
    # Для кратности 125 должно быть:
    # S ≡ 0 (mod 125)  ⟹  A + 22*(x+y) ≡ 0 (mod 125)
    # Вычислим A mod 125:
    r = A % 125  # A mod 125
    # Заметим, что A mod 125 = 1167165523 mod 125 = 23, так как 1167165523 - 125*9337324 = 23.
    # Условие:
    # 23 + 22*(x+y) ≡ 0 (mod 125)  ⟹  22*(x+y) ≡ -23 ≡ 102 (mod 125)
    # Так как 22 и 125 взаимно просты, умножим обе части на обратный элемент 22 по модулю 125.
    # Найдём обратный элемент для 22 по модулю 125.
    # Расширенным алгоритмом Евклида получаем: 22*108 ≡ templates1.ipynb (mod 125)
    # Тогда (x+y) ≡ 108*102 (mod 125)
    T_mod = (108 * 102) % 125  # 108*102 = 11016, 11016 mod 125 = 16.
    # Таким образом, x+y ≡ 16 (mod 125).
    # Так как x и y — цифры системы счисления с основанием 22, они принимают значения от 0 до 21,
    # следовательно, x+y может принимать значения от 0 до 42.
    # Единственное значение, удовлетворяющее условию, — 16.
    T = 16

    # Тогда S = A + 22*T = 1167165523 + 22*16 = 1167165523 + 352 = 1167165875.
    S = A + 22 * T

    # Проверяем, что S делится на 125:
    assert S % 125 == 0, "S не кратно 125"
    # Вычисляем частное:
    Q = S // 125

    # Выводим результат: частное от деления S на 125 в десятичной системе.
    return Q


if __name__ == "__main__":
    print("ANS:", main())
