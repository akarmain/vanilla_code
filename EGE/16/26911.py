from functools import lru_cache


@lru_cache
def f(n):
    if n == 0: return 0
    if n > 0 and n % 2 == 0: return f(n / 2) - 1
    if n > 0 and n % 2 != 0: return f(n - 1) + 1

def main():
    for i in range(0, 1001): f(i)

    ans = 0
    for i in range(1001):
        if f(i) == 0:
            ans += 1
    return ans


if __name__ == "__main__":
    print("ANS:", main())
