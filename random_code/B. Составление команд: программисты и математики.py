n, k, time = 0, 0, 0


def main():
    global n, k, time
    a, b = map(int, input().split())
    ans = 0
    for i in range(max(a, b)):
        if a - 3 > 0 and b - 1 > 0:
            ans += 1
            a -= 3
            b -= 1
        elif a - 1 > 0 and b - 3 > 0:
            ans += 1
            a -= 1
            b -= 3
        elif a - 2 > 0 and b - 2 > 0:
            ans += 1
            a -= 2
            b -= 2
    print(ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        main()

"""
2
1
1
0
2
500000000
"""
