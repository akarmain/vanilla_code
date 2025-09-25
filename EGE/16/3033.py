from functools import lru_cache
import sys

sys.setrecursionlimit(10 ** 7)


@lru_cache(maxsize=None)
def f(n):
    if n == 0:
        return 1
    if n > 0 and n % 2 == 0:
        return f(n - 1) + 1
    return f(n / 2)


def main():
    ans = 0
    for i in range(1, 5 * 10 ** 4 + 1):
        if f(i) == 3:
            ans += 1
    return ans


if __name__ == "__main__":
    print("ANS:", main())
