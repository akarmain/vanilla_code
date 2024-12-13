from collections import deque


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ts = [deque() for _ in range(k)]
    tg = n

    while tg > 0:
        dss = True
        while dss and tg > 0:
            dss = False
            if arr and arr[-1] == tg:
                arr.pop()
                tg -= 1
                dss = True
                continue

            for t in range(k):
                if ts[t] and ts[t][-1] == tg:
                    ts[t].pop()
                    tg -= 1
                    dss = True
                    break

        if tg == 0:
            break
        if tg > 0:
            if not arr:
                return "NO"
            w = arr.pop()
            if w == tg:
                tg -= 1
            else:
                placed = False
                for t in range(k):
                    if not ts[t] or w < ts[t][0]:
                        ts[t].appendleft(w)
                        placed = True
                        break
                if not placed:
                    return "NO"
                dss = True
                while dss and tg > 0:
                    dss = False

                    if arr and arr[-1] == tg:
                        arr.pop()
                        tg -= 1
                        dss = True
                        continue

                    for t in range(k):
                        if ts[t] and ts[t][-1] == tg:
                            ts[t].pop()
                            tg -= 1
                            dss = True
                            break

    if tg == 0:
        return "YES"
    return "NO"

"""
5 1
1 2 3 4 5

5 2
1 3 2 4 5

5 2
5 4 3 2
"""
if __name__ == '__main__':
    print(main())
