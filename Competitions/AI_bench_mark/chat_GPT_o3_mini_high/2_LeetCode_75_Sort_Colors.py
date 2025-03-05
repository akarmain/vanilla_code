def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def product_of_digits(n):
    product = 1
    for digit in n:
        product *= int(digit)
        if product > 10:  # Если произведение уже больше 10, нет смысла продолжать
            break
    return product

def count_simple_numbers(l, r):
    count = 0
    # Перебор всех чисел от l до r включительно
    for num in range(int(l), int(r) + 1):
        product = product_of_digits(str(num))
        if is_prime(product):
            count += 1
    return count

l = input().strip()
r = input().strip()

result = count_simple_numbers(l, r)
print(result)