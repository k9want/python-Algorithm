# dp[i] = dp[i-1] + dp[i-2]
n = int(input())
INF = 91
dp = [0] * INF
dp[1] = 1
dp[2] = 1
for i in range(3, INF):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
