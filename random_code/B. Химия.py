def main():
    n, k = map(int, input().split())
    k1 = 0
    s = input()
    for i in range(97, 123):
        if s.count(chr(i)) % 2 == 1:
            k1 += 1
    if k >= k1 - 1:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    for i in range(int(input())):
        main()
