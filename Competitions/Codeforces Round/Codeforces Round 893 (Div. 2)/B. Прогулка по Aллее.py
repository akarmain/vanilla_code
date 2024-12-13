def main():
    n, m, d = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.insert(0,1-d)
    arr.append(n + 1)
    ans = m
    for i in range(m + 1):
        ans += (arr[i + 1] - arr[i] - 1) // d
    ans1 = []
    for i in range(1, m + 1):
        ans1.append(ans - (arr[i + 1] - arr[i]-1)//d - (arr[i]-arr[i-1]-1)//d-1+(arr[i+1]-arr[i-1]-1)//d)
    x = min(ans1)
    print(x, ans1.count(x))


if __name__ == "__main__":
    for i in range(int(input())):
        main()