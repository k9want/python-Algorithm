# \ / 대각선으로 더하기
#자리수별로 0~9 개수를 찾아보고 규칙찾기

n = int(input())
INF = 101
dp = [[0] * 10 for _ in range(INF)]
dp[1][0] = 0

for i in range(1, 10):
    dp[1][i] = 1

for j in range(2, INF):
    for i in range(10):
        if i == 0:
            dp[j][i] = dp[j-1][i+1]
        elif i == 9:
            dp[j][i] = dp[j-1][i-1]
        else:
            dp[j][i] = dp[j-1][i-1] + dp[j-1][i+1]

print(sum(dp[n]) % 1000000000)