def main():
    n = int(input())

    if n < 1 or n > 50000:
        print(-2)
        return

    a = input().split()
    b = input().split()
    d = {}
    par = []
    val = []

    def get(x):
        if x not in d:
            d[x] = len(par)
            par.append(d[x])
            val.append(None)
        return d[x]

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    def join(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return True
        if val[x] is not None and val[y] is not None and val[x] != val[y]:
            return False
        par[y] = x
        if val[x] is None:
            val[x] = val[y]
        return True

    def put(x, num):
        x = find(x)
        if val[x] is not None and val[x] != num:
            return False
        val[x] = num
        return True

    ok = True

    for x, y in zip(a, b):
        nx = x.isdigit()
        ny = y.isdigit()

        if nx and ny:
            if x != y:
                ok = False
                break
        elif nx:
            if not put(get(y), x):
                ok = False
                break
        elif ny:
            if not put(get(x), y):
                ok = False
                break
        else:
            if not join(get(x), get(y)):
                ok = False
                break

    print('YES' if ok else 'NO')


if __name__ == '__main__':
    main()
