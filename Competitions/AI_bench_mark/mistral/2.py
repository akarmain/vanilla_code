def is_prime(n):
    """Проверяет, является ли число n простым."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def product_of_digits(n):
    """Вычисляет произведение цифр числа n."""
    product = 1
    while n > 0:
        product *= n % 10
        n //= 10
    return product

def count_simple_numbers(L, R):
    """Подсчитывает количество простоватых чисел в диапазоне от L до R включительно."""
    count = 0
    for number in range(L, R + 1):
        if is_prime(product_of_digits(number)):
            count += 1
    return count

# Чтение входных данных
L = int(input().strip())
R = int(input().strip())

# Подсчет и вывод количества простоватых чисел
print(count_simple_numbers(L, R))