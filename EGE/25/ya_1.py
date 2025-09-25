"""
URL: https://education.yandex.ru/ege/task/dc4c312e-1acd-406e-83a6-d4aac88cf80e
"""

def sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i, is_p in enumerate(primes) if is_p]


def algos(n):
    ...


def main():
    ...


if __name__ == "__main__":
    print("ANS:", resh(100))
