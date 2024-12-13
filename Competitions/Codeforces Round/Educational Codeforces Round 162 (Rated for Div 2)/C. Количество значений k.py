from math import gcd


def total_divisors(n):
    """Function to count the total number of divisors of n."""
    divisors = 1
    i = 2
    while i * i <= n:
        count = 1
        while n % i == 0:
            n //= i
            count += 1
        divisors *= count
        i += 1
    if n > 1:
        divisors *= 2
    return divisors


def solve(a, b, l):
    """Solves for the number of distinct possible values of k."""
    # Calculate the gcd of a and b
    common_gcd = gcd(a, b)
    # Divide l as much as possible by the gcd
    while gcd(l, common_gcd) != 1:
        l = l // gcd(l, common_gcd)

    # Get total divisors of the remaining part of l
    # This represents distinct values of k
    return total_divisors(l)


# Read number of test cases
t = int(input().strip())
for _ in range(t):
    a, b, l = map(int, input().strip().split())
    # Print the answer for each test case
    print(solve(a, b, l))