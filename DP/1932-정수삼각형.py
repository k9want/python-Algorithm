n = int(input())
dp = []

for i in range(n):
    dp.append(list(map(int, input().split())))


for j in range(1, n):
    for i in range(j+1):
        if i == 0:
            dp[j][i] = dp[j][i] + dp[j-1][i]
        elif i == j:
            dp[j][i] = dp[j][i] + dp[j-1][i-1]
        else:
            dp[j][i] = dp[j][i] + max(dp[j-1][i-1], dp[j-1][i])

result = 0
# print(dp)
for r in range(n):
    result = max(result, dp[n-1][r])
print(result)