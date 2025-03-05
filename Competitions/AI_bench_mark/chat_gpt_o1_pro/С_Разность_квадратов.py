import math


def main():
    d, l, r = map(int, input().split())
    count = 0

    # Пройдем по всем возможным делителям d
    for a in range(1, int(math.isqrt(d)) + 1):
        if d % a == 0:
            b = d // a
            # Мы должны, чтобы a < b, иначе меняем местами
            if a >= b:
                continue
            # Вычисляем x и y
            x = (a + b) // 2
            y = (b - a) // 2
            # Проверяем, что x и y - натуральные числа, а также что их квадраты подходят
            if (a + b) % 2 == 0 and (b - a) % 2 == 0 and x > 0 and y > 0:
                x2 = x * x
                y2 = y * y
                if l <= y2 < x2 <= r:
                    count += 1
    return count


if __name__ == '__main__':
    print(main())
