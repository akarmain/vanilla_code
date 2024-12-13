def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    chek = []
    for i in range(n):
        if a[i] in chek:
            print(chek)
            chek = []
            ans.append(i)
        else:
            chek.append(i)

    print(ans)
if __name__ == '__main__':
    for i in range(int(input())):
        print(main())
