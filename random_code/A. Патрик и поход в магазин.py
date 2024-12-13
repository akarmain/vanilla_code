def main():
    d1, d2, d3 = map(int, input().split())
    v1 = (d1 + d2) * 2
    v2 = (d1 + d3) * 2
    v3 = d1 + d3 + d2
    # v4 = d2 + d2 + d1 + d1
    # v5 = d2 + d3 + d1
    v6 = (d2 + d3) * 2
    return min(v1, v2, v3, v6)


if __name__ == "__main__":
    print(main())
