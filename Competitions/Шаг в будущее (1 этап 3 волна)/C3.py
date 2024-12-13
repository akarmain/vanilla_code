def main():
    n = int(input())
    pos = 1

    def to_minutes(t):
        hh, mm = t.split(':')
        return int(hh) * 60 + int(mm)

    intervals = []
    lengths = []
    for _ in range(n):
        ni = int(input())
        pos += 1
        cur = []
        length_set = None
        for __ in range(ni):
            line = input()
            pos += 1
            start_str, end_str = line.split('-')
            s = to_minutes(start_str)
            e = to_minutes(end_str)
            dur = e - s
            if length_set is None:
                length_set = dur
            else:
                pass
            cur.append((s, e))
        cur.sort(key=lambda x: x[0])
        intervals.append(cur)
        lengths.append(length_set)
    INF = 10 ** 9
    dp = [[(INF, INF, -1) for _ in intervals[0]]]
    for j, (s, e) in enumerate(intervals[0]):
        dp[0][j] = (0, s, -1)

    for i in range(1, n):
        dp.append([(INF, INF, -1)] * len(intervals[i]))
        for k, (sB, eB) in enumerate(intervals[i]):
            for j, (sA, eA) in enumerate(intervals[i - 1]):
                (w_prev, arr_prev, pprev) = dp[i - 1][j]
                if w_prev == INF:
                    continue
                if eA <= sB + 10:
                    add_wait = 0
                    if sB > eA:
                        add_wait = sB - eA
                    w_new = w_prev + add_wait
                    arr_new = arr_prev
                    old_w, old_arr, old_p = dp[i][k]
                    if (w_new < old_w) or (w_new == old_w and arr_new < old_arr):
                        dp[i][k] = (w_new, arr_new, j)

    best = (INF, INF, -1)
    best_idx = -1
    for j in range(len(intervals[n - 1])):
        (w, a, p) = dp[n - 1][j]
        if w < best[0] or (w == best[0] and a < best[1]):
            best = (w, a, p)
            best_idx = j

    chosen = [0] * n
    cur_idx = best_idx
    i = n - 1
    while i >= 0:
        chosen[i] = cur_idx
        cur_idx = dp[i][cur_idx][2]
        i -= 1
    total_waiting = 0
    chosen_intervals = [intervals[i][chosen[i]] for i in range(n)]
    s0, e0 = chosen_intervals[0]
    total_attendance = lengths[0]
    current_end = e0

    for i in range(1, n):
        sI, eI = chosen_intervals[i]
        if sI >= current_end:
            total_waiting += sI - current_end
            total_attendance += lengths[i]
            current_end = eI
        else:
            difference = current_end - sI
            if difference <= 5:
                total_attendance += (lengths[i] - difference)
                current_end = eI
            else:
                early = difference - 5
                total_attendance -= early
                total_attendance += (lengths[i] - 5)
                current_end = eI

    start_time = chosen_intervals[0][0]
    hh = start_time // 60
    mm = start_time % 60

    print(f"{hh:02d}:{mm:02d}")
    print(total_attendance)
    print(total_waiting)


if __name__ == '__main__':
    main()
