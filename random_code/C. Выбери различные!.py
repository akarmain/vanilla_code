def main():
    n, m, k = map(int, input().split())
    a = set(i for i in map(int, input().split()) if i <= k)
    b = set(i for i in map(int, input().split()) if i <= k)
    return len(a) >= k // 2 and len(b) >= k // 2 and len(a | b) >= k


if __name__ == "__main__":
    for _ in range(int(input())):
        print("YES" if main() else "NO")
