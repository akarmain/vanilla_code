n, a, b, c = map(int, input().split())
dp = [0] * (n+1)
dp[a] = 1
dp[b] = 1
dp[c] = 1
for i in range(2,n+1):
	if 1 - a > 0 and dp[i-a] > 0:
		dp[1] = max(dp[1], dp[1-a] + 1)
	if 1 - b > 0 and dp[i-b] > 0:
		dp[1] = max(dp[1], dp[1-6] + 1)
	if i - c > 0 and dp[i-c] > 0:
		dp[1] = max(dp[1], dp[i-c] + 1)
print(dp[n])