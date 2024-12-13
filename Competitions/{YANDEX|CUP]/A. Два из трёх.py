def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a // gcd(a, b) * b


def count(x, a, b, c, lcm_ab, lcm_ac, lcm_bc, lcm_abc):
    total = (x // lcm_ab + x // lcm_ac + x // lcm_bc) - 3 * (x // lcm_abc)
    return total


def main(n, a, b, c):
    lcm_ab = lcm(a, b)
    lcm_ac = lcm(a, c)
    lcm_bc = lcm(b, c)
    lcm_abc = lcm(lcm_ab, c)

    left = 1
    right = 10 ** 18
    result = -1

    while left <= right:
        mid = (left + right) // 2
        cnt = count(mid, a, b, c, lcm_ab, lcm_ac, lcm_bc, lcm_abc)
        if cnt >= n:
            if mid <= 10 ** 18:
                result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    n = int(input())
    print(main(n, a, b, c))
