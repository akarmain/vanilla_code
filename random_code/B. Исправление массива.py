def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(n-1, 0, -1):
        if arr[i-1] > arr[i]:
            arr.insert(i, arr[i-1] % 10)
            arr[i-1] = arr[i-1] // 10

    if arr == sorted(arr):
        print("YES")
        return
    print("NO")

if __name__ == "__main__":
    for i in range(int(input())):
        main()