def main():
    n = int(input())
    ans = []
    for _ in range(n):
        ans.append(input().find("#")+1)
    ans.reverse()
    print(*ans)

if __name__ == '__main__':
    for _ in range(int(input())):
        main()


