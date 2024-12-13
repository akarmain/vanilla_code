def simulate(L, obstacles):
    obs_s = sorted(obstacles, key=lambda x: x[0])

    cp = 0
    for x, hp in obs_s:
        di = x - cp
        md = min(di, 3)
        if md < hp:
            return x
        cp = x
    return L


def smi_he(L, a, b):
    mobs = []
    for i, (x, hp) in enumerate(a):
        if i == b:
            hp = hp // 2
        mobs.append((x, hp))
    return simulate(L, mobs)


def main():
    l = int(input())
    n = int(input())
    obsa = []
    idx = 2
    for _ in range(n):
        x, hp = map(int, input().split())
        idx += 2
        obsa.append((x, hp))
    obsa = sorted(obsa, key=lambda x: x[0])
    bebi = simulate(l, obsa)
    if bebi == l:
        print(0)
        print(l)
        return
    max_d = bebi
    chosn = 0

    for i, (x, hp) in enumerate(obsa):
        if hp == 1:
            pass
        dist = smi_he(l, obsa, i)
        if dist > max_d:
            max_d = dist
            chosn = x
        elif dist == max_d and dist != l:
            if x > chosn:
                chosn = x
        elif dist == max_d and dist == l:
            if x > chosn:
                chosn = x
    print(chosn)
    print(max_d)


if __name__ == "__main__":
    main()
