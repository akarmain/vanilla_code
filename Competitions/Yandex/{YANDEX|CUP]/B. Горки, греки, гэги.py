import threading

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())

        h_list = []
        while len(h_list) < n:
            h_list.extend(map(int, input().strip().split()))
        h = h_list[:n]

        inc = [1] * n
        for i in range(1, n):
            if h[i] > h[i - 1]:
                inc[i] = inc[i - 1] + 1
            else:
                inc[i] = 1

        dec = [1] * n
        for i in range(n - 2, -1, -1):
            if h[i] > h[i + 1]:
                dec[i] = dec[i + 1] + 1
            else:
                dec[i] = 1

        ans = 0
        for i in range(n):
            if inc[i] >= 2 and dec[i] >= 2:
                ans += (inc[i] - 1) * (dec[i] - 1)
        print(ans)

if __name__ == "__main__":
    threading.Thread(target=main).start()
