def main():
    n = int(input())
    s = input()
    return s.count("0")>0
if __name__ == '__main__':
    for _ in range(int(input())):
        print("YES" if main() else "NO")