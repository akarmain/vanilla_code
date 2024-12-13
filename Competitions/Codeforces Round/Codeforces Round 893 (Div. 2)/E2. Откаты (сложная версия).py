def main(t):
    s = input()
    his = []
    for i in range(t):
        his.append([])
    h = 0
    print(h, "h")
    if s[0] == "+":
        l = int(s[2])
        his[h+1].append(his[h]+[l])
        h += 1
        print(h, "h2")
    elif s[0] == "-":
        l = int(s[2])
        his[h+1] = his[h][:l]
        h += 1
    elif s[0] == "!":
        h -= 1
    else:
        c = []
        ans = 0
        for i in range(len(his[h])):
            if c in his[h][i]:
                c.append(his[h][i])
                ans += 1
        print(ans)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        main(t)

"""
3 1
4 1
4 4
6 4
5 2
7 7
1 1
51 1
"""
