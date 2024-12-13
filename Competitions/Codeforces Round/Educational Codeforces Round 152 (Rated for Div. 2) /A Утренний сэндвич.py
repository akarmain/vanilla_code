for rr in range(int(input())):
    b, c, h = map(int, input().split())
    ans = 0
    n = c+h
    if n > b:
        ans = b+(b-1)
    elif n < b:
        ans = n+(n+1)
    elif n == b:
        ans = b*2-1
    print(ans)