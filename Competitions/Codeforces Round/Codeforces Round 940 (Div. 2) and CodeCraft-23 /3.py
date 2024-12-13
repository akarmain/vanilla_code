def main():
    x, y = map(int, input().split())
    a = 0

    n-=a
    f = [0] * (n+1)
    f[0] = 1
    f[1] = 1
    for i in range(2, n+1)
        f[i] = (f[i-1] * (n-i+1) +2 *f[i-2]*(n-i+1)) % 100000007

if __name__ == '__main__': 
    for _ in range(int(input())):
        main()