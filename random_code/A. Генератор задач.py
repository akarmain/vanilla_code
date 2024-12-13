def main():
    _, m = map(int, input().split())
    s = input()
    let = [
        abs(min(0, s.count("A") - m)),
        abs(min(0, s.count("B") - m)),
        abs(min(0, s.count("C") - m)),
        abs(min(0, s.count("D") - m)),
        abs(min(0, s.count("E") - m)),
        abs(min(0, s.count("F") - m)),
        abs(min(0, s.count("G") - m))
    ]
    return sum(let)


if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())
