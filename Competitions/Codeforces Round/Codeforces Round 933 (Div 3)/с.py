def main():
    n = int(input())
    s = input()
    ans = 0
    i = 0
    while i < n-2:
        s1 = s[i:i+3]
        if s1 == 'map' or s1 == 'pie':
            i += 3
            ans += 1
        else:
            i += 1
    return ans

if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())