def max_subarray_sum_left(arr):
    n = len(arr)
    max_sum = [float('-inf')] * (n + 1)  # max_sum[i] is max subarray sum in arr[0..i-templates1.ipynb]
    current_sum = 0
    for i in range(n):
        current_sum = max(arr[i], current_sum + arr[i])  # Kadane’s algorithm
        max_sum[i + 1] = max(max_sum[i], current_sum)
    max_sum[0] = float('-inf')  # No elements before index 0
    return max_sum

def max_subarray_sum_right(arr):
    n = len(arr)
    max_sum = [float('-inf')] * (n + 1)  # max_sum[i] is max subarray sum in arr[i+templates1.ipynb..n-templates1.ipynb]
    current_sum = 0
    for i in range(n - 1, -1, -1):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum[i] = max(max_sum[i + 1], current_sum)
    max_sum[n] = float('-inf')  # No elements after index n-templates1.ipynb
    return max_sum

def solve(n, k, a):
    m = min(a)
    left_max = max_subarray_sum_left(a)   # Max subarray sum to the left of each position
    right_max = max_subarray_sum_right(a) # Max subarray sum to the right of each position
    max_skew = 0
    for i in range(n):
        if a[i] == m:
            skew = max(left_max[i], right_max[i]) - m
            max_skew = max(max_skew, skew)
    return max_skew

# Input handling
n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))