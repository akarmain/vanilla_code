def main():
    n, k = map(int, input().split())
    x = 1
    if n == 1:
        print(k)
        pass
    if n < 4:
        return [k] + [0] * (n-1)
    while x <= k:
        x *= 2
    x //= 2
    a = []
    a.append(x-1)
    k -= x-1
    a.append(k // 2)
    a.append(k // 2 + k%2)
    if len(a) < n:
        a +=(n - len(a)) * [0]

    return a


if __name__ == '__main__':
    for _ in range(int(input())):
        print(*main())
