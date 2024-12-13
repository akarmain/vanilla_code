def main():
    n, k, x = map(int, input().split())
    f1 = (k*(k+1))/2
    f2 = (((n-k+1)+n)*k)/2
    return f1 <= x <= f2

if __name__ == '__main__':
    for _ in range(int(input())):
        print("YES" if main() else "NO")
