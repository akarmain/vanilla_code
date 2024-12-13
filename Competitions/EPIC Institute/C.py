def k_sort(test_cases):
    results = []
    for n, a in test_cases:
        coins = 0
        max_gap = 0

        for i in range(n - 1):
            if a[i] > a[i + 1]:
                max_gap = max(max_gap, a[i] - a[i + 1])

        results.append(max_gap)

    return results


# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get the results
results = k_sort(test_cases)

# Print the results
for result in results:
    print(result)
