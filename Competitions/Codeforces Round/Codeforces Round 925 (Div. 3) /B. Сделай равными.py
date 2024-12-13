def main():
    n = int(input())
    a = list(map(int, input().split()))
    sr = sum(a) // n
    s = 0
    for x in a:
        if x >= sr:
            s += x - sr
        else:
            if s >= sr - x:
                s -= (sr - x)
            else:
                print("NO")
                break
    else:
        print("YES")


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
