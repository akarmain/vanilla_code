def main():
    n, m = map(int, input().split())
    d = int(input()) - 1
    maze = []
    sr = sc = 0
    for i in range(n):
        r = list(input())
        for j in range(m):
            if r[j] == '1':
                sr, sc = i, j
        maze.append(r)
    st = 0
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    r, c = sr, sc
    v = {(r, c, d)}
    while True:
        if maze[r][c] == 'f':
            print(st)
            return
        ld = (d + 3) % 4
        nr = r + dirs[ld][0]
        nc = c + dirs[ld][1]
        if maze[nr][nc] != 'x':
            d = ld
            r, c = nr, nc
            st += 1
        else:
            nr = r + dirs[d][0]
            nc = c + dirs[d][1]
            if maze[nr][nc] != 'x':
                r, c = nr, nc
                st += 1
            else:
                rd = (d + 1) % 4
                nr = r + dirs[rd][0]
                nc = c + dirs[rd][1]
                if maze[nr][nc] != 'x':
                    d = rd
                    r, c = nr, nc
                    st += 1
                else:
                    d = (d + 2) % 4
        if (r, c) == (sr, sc) and st > 0:
            print(st)
            return
        if (r, c, d) not in v:
            v.add((r, c, d))


if __name__ == "__main__":
    main()
