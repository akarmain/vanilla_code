def main():
    from collections import deque

    n, m = map(int, input().split())
    lab = [list(input()) for _ in range(n)]

    start1 = None
    start2 = None
    finish = None
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 'templates1.ipynb':
                start1 = (i, j)
            elif lab[i][j] == '2':
                start2 = (i, j)
            elif lab[i][j] == 'f':
                finish = (i, j)
    if start1 is None or start2 is None or finish is None:
        print(-1)
        return


    fr, fc = finish

    r1, c1 = start1
    r2, c2 = start2
    visited = {}
    visited[(r1, c1, r2, c2)] = k0

    q = deque()
    q.append((0, r1, c1, r2, c2, k0))


    while q:
        t, r1, c1, r2, c2, k = q.popleft()

        if (r1, c1) == (fr, fc) and (r2, c2) == (fr, fc):
            print(t)
            return

        for dr1, dc1 in moves:
            nr1, nc1 = r1 + dr1, c1 + dc1
            if dr1 == 0 and dc1 == 0:
                nr1, nc1 = r1, c1

            if not (0 <= nr1 < n and 0 <= nc1 < m):
                continue
            cell1 = lab[nr1][nc1]

            nk1 = k
            if cell1 == 'x':
                continue
            elif cell1 == 'k':
                nk1 = k + 1
            elif cell1 == 'd':
                if k > 0:
                    nk1 = k - 1
                else:
                    continue
            else:
                nk1 = k

            for dr2, dc2 in moves:
                nr2, nc2 = r2 + dr2, c2 + dc2
                if dr2 == 0 and dc2 == 0:
                    nr2, nc2 = r2, c2

                if not (0 <= nr2 < n and 0 <= nc2 < m):
                    continue
                cell2 = lab[nr2][nc2]

                nk2 = nk1
                if cell2 == 'x':
                    continue
                elif cell2 == 'k':
                    nk2 = nk1 + 1
                elif cell2 == 'd':
                    if nk1 > 0:
                        nk2 = nk1 - 1
                    else:
                        continue
                else:
                    nk2 = nk1

                state = (nr1, nc1, nr2, nc2)
                if state in visited:
                    if visited[state] >= nk2:
                        continue
                visited[state] = nk2

                q.append((t + 1, nr1, nc1, nr2, nc2, nk2))

    print(-1)


if __name__ == '__main__':
    ... # Не работает
    # main()
