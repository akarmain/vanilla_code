for _ in range(int(input())):
    s = input().strip()
    r = ['0'] * len(s)
    k = len(s)
    t = 0
    for i in range(len(s), 0, -1):
        c = ord(s[i - 1]) + t
        t = c >= ord('5')
        if t:
            k = i
        else:
            r[i - 1] = chr(c)
    if t:
        print('1' + '0' * len(s))
    else:
        print(''.join(r[:k]) + '0' * (len(s) - k))
