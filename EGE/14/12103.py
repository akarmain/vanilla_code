def main():
    f = 361 * 2349 ** 84 - 89 ** 192 + 1953 ** 481 * 4843 ** 151
    ans = 0
    while f > 0:
        if f % 9 == 5:
            ans += 1
        f //= 9
    return ans


if __name__ == "__main__":
    print("ANS:", main())
