MOD = 10 ** 9 + 7
MAXN = 2 * 10 ** 6 + 5
factorials = [1] * MAXN
inv_factorials = [1] * MAXN


def precompute_factorials():
    for i in range(1, MAXN):
        factorials[i] = (factorials[i - 1] * i) % MOD
    inv_factorials[MAXN - 1] = pow(factorials[MAXN - 1], MOD - 2, MOD)
    for i in range(MAXN - 2, -1, -1):
        inv_factorials[i] = (inv_factorials[i + 1] * (i + 1)) % MOD


def comb(n, k):
    if k < 0 or k > n:
        return 0
    return (factorials[n] * inv_factorials[k] % MOD) * inv_factorials[n - k] % MOD


def main():
    a, b = map(int, input().split())
    precompute_factorials()

    total = 0

    k_min = (b + 1) // 2  # Ceiling division
    k_max = min(b, a - 1)

    for k in range(k_min, k_max + 1):
        s = b - k
        if s < 0 or s > k:
            continue
        extra_P = a - (k + 1)
        if extra_P < 0:
            continue
        ways_T = comb(k, s)
        ways_P = comb(extra_P + k, k)
        total = (total + ways_T * ways_P) % MOD

    return int(total)


if __name__ == "__main__":
    print(main())
