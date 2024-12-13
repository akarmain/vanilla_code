def main():
    l, k, u = map(int, input().split())
    n = int(input())
    idx = 4
    ovs = []
    for _ in range(n):
        x, hp = map(int, input().split())
        idx += 2
        ovs.append((x, hp))
    ovs.sort(key=lambda x: x[0])

    d_co = int(input())
    idx += 1
    doors = []
    for _d in range(d_co):
        d = int(input())
        idx += 1
        doors.append(d)
    doors.sort()

    def beff(x):
        left, right = 0, len(doors) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if doors[mid] < x:
                res = doors[mid]
                left = mid + 1
            else:
                right = mid - 1
        return res

    cop = 0
    for x, hp in ovs:
        d = beff(x)
        if d == -1:
            epna = max(cop, 0, x - k)
        else:
            epna = max(cop, 0, x - k, d)

        saa = x - epna
        if saa * u < hp:
            print(x)
            return
        cop = x
    print(l)


if __name__ == "__main__":
    main()
