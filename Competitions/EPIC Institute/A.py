def main():
    n, k = map(int, input().split())
    l = ([1]+[0]*(k-1))*n
    return len(l)-k+1


if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())
