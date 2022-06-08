"""
dp[i] = max(dp[i], p[i] + dp[i-k]
"""

n = int(input())
p = [0]
p += list(map(int, input().split()))
dp = [0] * (n+1)
for j in range(1, n+1):
    for i in range(1, j+1):
        dp[j] = max(dp[j], dp[j-i] + p[i])

print(dp[j])