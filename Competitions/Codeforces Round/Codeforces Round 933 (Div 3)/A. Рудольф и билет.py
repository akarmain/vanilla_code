def main():
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(0, n - 3):
        if arr[i] < 0:
            return False
        arr[i + 1] -= 2 * arr[i]
        arr[i + 2] -= arr[i]
        
    return arr[-1] == 0 and arr[-2] == 0


"""
3
5
1 3 5 5 2
5
2 4 4 5 1
5
0 1 3 3 1
"""

if __name__ == '__main__':
    for _ in range(int(input())):
        print("YES" if main() else "NO")
