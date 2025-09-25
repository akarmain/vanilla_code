def f(n):
    if n == 0: return 0
    if n % 2 == 0 and n >0:
        return f(n / 2)
    return f(n - 1) + 1


def main():
    ans = 0
    for i in range(1, 501):
        if f(i) == 8:
            ans += 1
    return ans


if __name__ == "__main__":
    print("ANS:", main())
