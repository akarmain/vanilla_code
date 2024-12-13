def min_coins_to_red(n, arr):
    coins_spent = 0

    for i in range(n):
        if arr[i] == 0:
            continue

        if arr[i] == 1:
            if i < n - 1 and arr[i + 1] == 0:
                coins_spent += 1
                arr[i + 1] = 1

        elif arr[i] == 2:
            if i < n - 1 and arr[i + 1] == 0:
                coins_spent += 1
                arr[i + 1] = 1
            coins_spent += 1
            arr[i] = 1

    return coins_spent

n = int(input())
arr = list(map(int, input().split()))

ans = min_coins_to_red(n, arr)
print(ans)
