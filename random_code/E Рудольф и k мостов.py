def D(a,n,d):
	dp = [999999999999] * n
	dp[0] = a[0] + 1
	for i in range(1,n):
		x = min(dp[max(0,i-d-1):i])
		dp[i] = x + a[i] + 1
	return (dp[n-1])


for __ in range(int(input())):
	n, m, k, d = map(int, input().split())
	s = [0] * n
	for i in range(n):
		a = list(map(int, input().split()))
		s[i] = D(a,m,d)
	ans = 10000000000000
	for i in range(n-k+1):
		ans = min(ans, sum(s[1:1+k]))
	print(ans)