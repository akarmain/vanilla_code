def main():
    global n, k
    n = int(input())
    arr = list(map(int, input().split()))
    j = 0
    for i in range(n):
        j -= 1
        print(arr[i]-arr[j], end="")


if __name__ == "__main__":
    for i in range(int(input())):
        print("YES" if main() else "NO")
        print()