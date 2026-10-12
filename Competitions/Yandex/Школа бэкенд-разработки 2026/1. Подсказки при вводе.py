import heapq


def main():
    n, k = map(int, input().split())

    if n < 1 or n > 100000 or k < 1 or k > 100000:
        print(-2)
        return

    arr = {}

    for _ in range(n):
        s = input()
        arr.setdefault(s[0], []).append((0, s))

    for h in arr.values():
        heapq.heapify(h)

    ans = []

    for _ in range(k):
        c = input()
        h = arr[c]
        cnt, s = heapq.heappop(h)
        ans.append(s)
        heapq.heappush(h, (cnt + 1, s))

    print('\n'.join(ans))


if __name__ == '__main__':
    main()
