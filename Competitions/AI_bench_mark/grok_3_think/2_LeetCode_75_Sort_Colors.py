def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def product_of_digits(n):
    prod = 1
    for d in n:
        prod *= int(d)
    return prod

def count_simple_numbers(l, r):
    count = 0
    for num in range(int(l), int(r) + 1):
        prod = product_of_digits(str(num))
        if is_prime(prod):
            count += 1
    return count

l = input().strip()
r = input().strip()

result = count_simple_numbers(l, r)
print(result)