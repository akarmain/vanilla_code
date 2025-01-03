# https://codeforces.com/contest/2008/problem/A
def main():
    a, b = map(int, input().split())
    if a % 2 == 1:
        return False
    if a == 0 and b % 2 == 1:
        return False
    return True


if __name__ == '__main__':
    for _ in range(int(input())):
        print("YES" if main() else "NO")
