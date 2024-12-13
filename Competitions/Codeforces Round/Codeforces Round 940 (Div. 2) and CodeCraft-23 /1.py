def main():
    n = int(input())
    k = [0] * 101
    a = list(map(int, input().split()))
    for x in a:
        k[x] += 1
    ans = 0
    for i in range(1, 101):
        ans += k[i]//3
    return ans
if __name__ == '__main__':
    for i in range(int(input())):
        print(main())