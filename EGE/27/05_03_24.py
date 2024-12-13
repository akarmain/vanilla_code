def main():
    f = open('27-A.txt', 'r')
    n = int(f.readline())
    ans = 0
    m1 = [0] * 102
    a = [int(i) for i in f]
    for i in range(1, n):
        m1[a[i-1] %102] = max(a[i-1], m1[i-2] %102)
        ans = max(ans, a[i]+m1[(102 - a[i-1]%102)%102])
    print(ans)

if __name__ == '__main__':
    main()
