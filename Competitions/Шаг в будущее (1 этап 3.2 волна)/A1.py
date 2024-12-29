def solve():
    l = int(input())
    n = int(input())

    сс = []
    idx = 2
    for _ in range(n):
        c, hp = map(int, input().split())
        сс.append((c, hp))
        idx += 2
    сс.sort(key=lambda x: x[0])

    def пв(obstacles, removed_index):
        for i, (c, hp) in enumerate(obstacles):
            if i == removed_index:
                continue
            asd = 2 * min(c, 4)
            if asd < hp:
                return c
        return l

    kal = пв(сс, -1)
    if kal == l:
        print(0)
        print(l)
        return
    shs = kal
    aall = -1
    for i in range(n):
        dist_i = пв(сс, i)
        if dist_i > shs:
            shs = dist_i
            aall = i
        elif dist_i == shs:
            if сс[i][0] > сс[aall][0]:
                aall = i

    if aall == -1:
        print(0)
        print(shs)
    else:
        print(сс[aall][0])
        print(shs)


if __name__ == '__main__':
    solve()
