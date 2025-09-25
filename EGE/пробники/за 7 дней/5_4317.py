def to5(x):
    ans = ""
    while x:
        ans = str(x % 5) + ans
        x //= 5
    return ans


def algos(n):
    n5 = to5(n)
    if (n % 10) % 2 == 0:
        return int(f"{n5}2", 5)
    return int(f"2{n5}3", 5)


def main():
    for n in range(1, 1000000000000000):
        if algos(n) < 1000:
            print(n, algos(n))


if __name__ == "__main__":
    print("ANS:", main())
