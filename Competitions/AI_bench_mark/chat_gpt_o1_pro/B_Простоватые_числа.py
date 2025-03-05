def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    l = int(input().strip())
    r = int(input().strip())

    primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    count = 0

    for num in range(l, r + 1):
        prod = 1
        for digit in str(num):
            prod *= int(digit)
        if prod in primes:
            count += 1

    return count


if __name__ == '__main__':
    print(main())
