def main():
    a, b, c = map(int, input().split())
    a, b = max(a, b), min(a, b)
    ans = 0
    while a > b:
        a -= c
        b += c
        ans += 1
    return ans


if __name__ == "__main__":
    for _ in range(int(input())):
        print(main())
