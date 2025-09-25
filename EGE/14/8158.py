from string import printable


def to_15(n):
    ans = ""
    while n:
        ans = printable[n % 15] + ans
        n //= 15
    return ans


def main():
    for x in reversed('01234567abcde'):
        if (int(f"1{x}51", 15) - int(f"3{x}2", 15)) % 4 == 0:
            return int((int(f"1{x}51", 15) - int(f"3{x}2", 15)) / 4)


if __name__ == "__main__":
    print("ANS:", main())
