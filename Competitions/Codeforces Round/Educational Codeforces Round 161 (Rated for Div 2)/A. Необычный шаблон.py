def main():
    n = int(input())
    a = input()
    b = input()
    c = input()
    for i in range(n):
        if a[i] != b[i]:
            if c[i] != a[i] and c[i] != b[i]:
                return True
        else:
            if c[i] != a[i]:
                return True
    return False

if __name__ == '__main__':
    for _ in range(int(input())):
        print("YES" if main() else "NO")