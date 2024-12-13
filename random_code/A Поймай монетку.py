def main():
    x, y = map(int, input().split())
    return y >= -1


if __name__ == '__main__':
    for _ in range(int(input())):
        print("YES" if main() else "NO")
