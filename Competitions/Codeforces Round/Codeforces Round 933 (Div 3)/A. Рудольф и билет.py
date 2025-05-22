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
templates1.ipynb 3 5 5 2
5
2 4 4 5 templates1.ipynb
5
0 templates1.ipynb 3 3 templates1.ipynb
"""

if __name__ == '__main__':
    for _ in range(int(input())):
        print("YES" if main() else "NO")
