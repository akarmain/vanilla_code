def main():
    n = int(input())
    s = sum(list(map(int, input().split())))
    if s**0.5 == int(s**0.5):
        print("YES")
        return
    print("NO")

if __name__ == '__main__':
    for _ in range(int(input())):
        main()