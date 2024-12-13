def rec(s):
    global ans
    if len(s) == 12:
        ans+=1
        return
    a = int(s[-1])
    if a%2 == 0:
        for i in range(a+2, 9, 2):
            rec(s+str(i))
        for i in range(a-1, -1, 2):
            rec(s + str(i))


def main():
    for i in range(10)
        rec(s)

if __name__ == '__main__':
    main()