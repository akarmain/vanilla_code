def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    if sum(a)<=k:
        return n



    k1 = (k+1)//2
    for i in range(n):
        if k1 >= a[i]:
            ans += 1
            k1 -= a[i]
        else:
            break

    k1 = k // 2
    for i in range(n-1, -1, -1):
        if k1 >= a[i]:
            ans += 1
            k1 -= a[i]
        else:
            break
    return ans


    # i0 = 0
    # i1 = n-templates1.ipynb
    # for i in range(k):
    #     if i%2 == 0:
    #         a[i0] -=templates1.ipynb
    #         if a[i0] == 0:
    #             ans += templates1.ipynb
    #             i0 +=templates1.ipynb
    #     else:
    #         a[i1] -= templates1.ipynb
    #         if a[i1] == 0:
    #             ans += templates1.ipynb
    #             i1 -=templates1.ipynb
    # return ans

if __name__ == '__main__':
    for _ in range(int(input())):
        print(main())