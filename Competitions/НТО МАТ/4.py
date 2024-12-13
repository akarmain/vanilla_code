import math


def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


def calculate_k(n):
    divisors = sorted(get_divisors(n))
    product = 1
    print(divisors, len(divisors))
    # Умножаем делители с учетом их количества
    for divisor in divisors:
        product *= divisor

    # Вычисляем k из произведения делителей
    k = math.log10(product)
    return int(k)


number = 1000
k = calculate_k(number)
print(f"Значение k для произведения всех делителей числа {number}: {k}")
