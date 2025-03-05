"""
URL:

"""
import sys

sys.setrecursionlimit(9999999)


def f(n):
    if n <= 1:
        return 1
    elif n % 2 == 0:
        return (n // 2) * f(n - 1)
    else:
        return ((n - 1) // 2) * f(n - 1)

def main():
    return (f(2024) - f(2022)) / f(2021)


if __name__ == "__main__":
    print("ANS:", int(main()))
