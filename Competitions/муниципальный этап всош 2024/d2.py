from bisect import bisect_left


def main():
    n, k = map(int, input().split())
    ws = list(map(int, input().split()))
    fs = []
    for w in reversed(ws):
        pos = bisect_left(fs, w + 1)
        if pos == len(fs):
            if len(fs) == k:
                print("NO")
                return
            fs.append(w)
        else:
            fs[pos] = w
    print("YES")


if __name__ == '__main__':
    main()
