def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))
    ans = [0] * (n+1)
    s = 0
    for i in range(n):
        ans[abs(x[i])] += a[i]
    for i in range(1, n+1):
        s += k
        s -= ans[i]
        if s < 0:
            return False
    return True


if __name__ == '__main__':
    for _ in range(int(input())): print("YES" if main() else "NO")