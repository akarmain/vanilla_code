from collections import Counter


def main():
    k = int(input())
    n = int(input())
    pr = [input().strip() for _ in range(n)]
    m_c = k // 4
    p_c = Counter(pr)
    sp = [pt for pt, c in p_c.items() if c >= m_c]
    if sp:
        for i in sorted(sp):
            print(i)
    else:
        print("NO")


if __name__ == "__main__":
    main()
