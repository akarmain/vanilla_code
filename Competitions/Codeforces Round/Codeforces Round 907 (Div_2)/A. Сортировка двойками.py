def main():
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n - 1):
        c = i+1
        if arr[i] > arr[i + 1] and not ((c & (c-1) == 0) and c != 0):
            return False
    return True

if __name__ == '__main__':
    for _ in range(int(input())):
        print("Yes" if main() else "NO")
