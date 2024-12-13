def main():
    a = input()
    b = input()
    n = len(a)
    m = len(b)
    ans = n + m

    for i in range(m):
        j = i
        for c in a:
            if j < m and c == b[j]:
                j += 1
        ans = min(ans, n + m - (j - i))
    return ans


if __name__ == "__main__":
    for _ in range(int(input())):
        print(main())
