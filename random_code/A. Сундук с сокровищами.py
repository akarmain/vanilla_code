def main():
    x, y, k = map(int, input().split())
    if x > y:
        return x
    return y+max(0, y-(x+k))


if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())
