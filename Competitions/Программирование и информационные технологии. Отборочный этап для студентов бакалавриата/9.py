def main():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    last_pos = {}
    left = 0
    ans = 0

    for right, x in enumerate(arr):
        if x in last_pos and last_pos[x] >= left:
            left = last_pos[x] + 1
        last_pos[x] = right
        ans += right - left + 1
    return ans


if __name__ == "__main__":
    for _ in range(int(input())):
        print(main())
