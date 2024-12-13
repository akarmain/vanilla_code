def main():
    n, c, d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    new_a = []
    for i in range(n):
        for j in range(n):
            new_a.append(a[0]+i*c+j*d)
    new_a.sort()
    print("YES" if new_a == a else "NO")
    
if __name__ == '__main__':
    for _ in range(int(input())):
        main()