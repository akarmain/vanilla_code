import math

def fermat_factorization(n: int) -> list[int]:
    # Если число чётное — выносим 2 и продолжаем с нечётной частью
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Если после деления осталось 1 — значит, всё уже разложено
    if n == 1:
        return factors

    # Инициализируем a — ближайшее целое к корню из N вверх
    a = math.ceil(math.sqrt(n))
    b2 = a * a - n

    # Пока b^2 не станет полным квадратом, увеличиваем a
    while not math.isqrt(b2) ** 2 == b2:
        a += 1
        b2 = a * a - n

    b = math.isqrt(b2)
    p = a - b
    q = a + b

    # Добавляем найденные множители
    factors.append(p)
    factors.append(q)
    return factors

# Пример:
N = 54
print(f"Разложение {N} по Ферма: {fermat_factorization(N)}")
