def main():
    n, m, k = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    markers = {}
    for _p in range(p):
        t, r, c = input().strip().split(';')
        t, r, c = int(t), int(r), int(c)
        markers[(r - 1, c - 1)] = t
    r, c = n - 1, k - 1
    dx, dy = -1, 0

    visited = set()
    ttim = 0

    while 0 <= r < n and 0 <= c < m:
        if (r, c) in visited:
            print(r + 1, c + 1)
            print(ttim)
            return
        visited.add((r, c))
        ttim += field[r][c]
        if (r, c) in markers:
            t = markers[(r, c)]
            if t == 1:
                if dx == -1 and dy == 0:
                    dx, dy = 0, -1
                elif dx == 1 and dy == 0:
                    dx, dy = 0, 1
                elif dx == 0 and dy == -1:
                    dx, dy = -1, 0
                elif dx == 0 and dy == 1:
                    dx, dy = 1, 0
            if t == 2:
                if dx == -1 and dy == 0:
                    dx, dy = 0, 1
                elif dx == 1 and dy == 0:
                    dx, dy = 0, -1
                elif dx == 0 and dy == -1:
                    dx, dy = 1, 0
                elif dx == 0 and dy == 1:
                    dx, dy = -1, 0
        r += dx
        c += dy
    print(0)
    print(ttim)


if __name__ == '__main__':
    main()
