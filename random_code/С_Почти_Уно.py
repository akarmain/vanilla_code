def main():
    s1 = input()
    s2 = list(map(str, input().split()))
    ans = []
    for i in range(5):
        if (s2[i][0] == s1[0]) or s2[i][0] == "b" or (s2[i][1] == s1[1]):
            ans.append(i+1)
    if len(ans) == 0:
        print("NO")
    else:
        print("YES")
        print(*ans)
if __name__ == '__main__':
    main()
