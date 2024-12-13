def is_power_of_two(n):
    return n != 0 and ((n & (n - 1)) == 0)


def get_divisors(n):
    divisors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors


def optimized_count_bits_algorithm(n):
    if is_power_of_two(n):
        sqrt_n = int(n ** 0.5)
        divisors_of_sqrt_n = get_divisors(sqrt_n)
        return 2 * len(divisors_of_sqrt_n)

    cnt = 0
    divisors = get_divisors(n)
    for i in divisors:
        if i * i > n:
            break
        if n & i == 0:
            cnt += 1
            if i * i != n:
                cnt += 1
    return cnt



if __name__ == '__main__':
    arr = []
    for i in range(int(input())):
        arr.append(int(input()))
    ans = [optimized_count_bits_algorithm(n) for n in arr]
    for i in ans:
        print(i)
