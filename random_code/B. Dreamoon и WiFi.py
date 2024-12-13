def factorial(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

def C(n, k):
    return factorial(n) / ((factorial(n)) * (factorial(n - k)))

def main():
    m = list(input())
    k = list(input())
    p = 0
    v = 0
    cq = 0
    for i in m:
        if i == "+":
            p += 1
        elif i == "-":
            p -= 1

    for i in k:
        if i == "+":
            v += 1
        elif i == "-":
            v -= 1
        else:
            cq += 1

    if cq == 0 and p==v:
        return float(1)
    print(p, v)
    print(cq)

if __name__ == '__main__':
    print(main())
