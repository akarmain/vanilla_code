def par(n):
    ...


def main():
    n, k = map(int, input().split())
    n1 = n - k + 1
    ans_max = n1 * (n1 - 1) // 2
    n1 = n // k
    n2 = n % k
    ans_min = (((n1 + 1) * n1) // 2) * n2 + (k - n2) * (((n1 - 1) * n1) // 2)
    return ans_min, ans_max


if __name__ == '__main__':
    print(*main())
