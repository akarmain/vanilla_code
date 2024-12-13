def main():
    n = int(input())
    r_1 = list(map(int, input().rstrip().split()))
    r_2 = list(map(int, input().rstrip().split()))

    a_1 = 0
    a_2 = 0
    for i in range(n):
        if r_1[i] > r_2[i]:
            a_1 += r_1[i]
        elif r_2[i] > r_1[i]:
            a_2 += r_2[i]

    for i in range(n):
        if r_1[i] == r_2[i] == 1:
            if a_1 > a_2:
                a_2 += 1
            else:
                a_1 += 1
        elif r_1[i] == r_2[i] == -1:
            if a_1 > a_2:
                a_1 -= 1
            else:
                a_2 -= 1
    return min(a_1, a_2)


if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())
