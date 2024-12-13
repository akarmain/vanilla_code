import heapq
import sys
from itertools import combinations


def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    E = int(sys.stdin.readline())
    init_times = [A, B, C, D]
    n = 4

    init_state = (tuple([False] * n), (0, 0, 0, 0), False)
    goal = tuple([True] * n)

    pq = []
    heapq.heappush(pq, (0, init_state))

    vis = {}

    while pq:
        t, s = heapq.heappop(pq)
        pos, cnt, side = s

        if pos == goal and side:
            print(t)
            return

        sk = (pos, cnt, side)
        if sk in vis and vis[sk] <= t:
            continue
        vis[sk] = t

        side_p = [i for i in range(n) if pos[i] == side]

        for num in [1, 2]:
            for ppl in combinations(side_p, num):
                ct = []
                cnt_new = list(cnt)
                for p in ppl:
                    k = cnt[p]
                    c_t = init_times[p] + k * E
                    ct.append(c_t)
                    cnt_new[p] += 1
                t_cross = max(ct)

                pos_new = list(pos)
                for p in ppl:
                    pos_new[p] = not pos[p]

                new_side = not side
                s_new = (tuple(pos_new), tuple(cnt_new), new_side)
                t_new = t + t_cross

                sk = (s_new[0], s_new[1], s_new[2])
                if sk in vis and vis[sk] <= t_new:
                    continue

                heapq.heappush(pq, (t_new, s_new))
    print("404 )")


if __name__ == "__main__":
    main()
