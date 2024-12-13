def inv(x):
    d = (1 << 31) - 1
    return d ^ x

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    col = {}
    ans = 0

    for x in arr:
        b = inv(x)
        if col.get(x, 0) == 0:
            ans += 1
            col[b] = col.get(b, 0) + 1
        else:
            col[x] -= 1

    return ans


if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())
