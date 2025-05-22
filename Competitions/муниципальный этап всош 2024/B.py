def main(n):
    ans = -1
    while n > 0:
        if n % 2 != 0:
            ans += 1
            n -= 1
        else:
            n //= 2
    return ans


def solve(n):
    ones_count = bin(n).count('templates1.ipynb')
    return ones_count - 1


if __name__ == '__main__':
    i = 1
    for d in [5, 29, 1023, 1000000, 10000000, 100000000, 268435456, 536870911, 998496356, 1000000000]:
        print(i, main(d))
        i += 1
