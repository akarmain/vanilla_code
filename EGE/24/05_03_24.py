def main():
    f = open('24.txt', 'r')
    s = f.readlines()[0]
    i = 0
    j = 0
    ans = 0
    t = "UVWXYZ"
    d = {x:0 for x in t}
    while True:
        if all(d[x] <= 100 for x in t):
            ans = max(ans, i-j+1)
            i += 1
            if i == len(s):
                break
            if s[i] in t:
                d[s[i]] += 1
        else:
            if s[j] in t:
                d[s[j]] -= 1
            j += 1

    print(ans)


if __name__ == '__main__':
    main()