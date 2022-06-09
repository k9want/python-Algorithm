"""
2차원 dp 초기 셋팅을 할 때 반복문으로 해야할 경우도 잇다는 점!!
규칙을 찾을때는 1부터 작은 수부터 차례대로 이어나가면서 규칙을 찾는다.
"""
n, k = map(int, input().split())

dp = [[0] * 201 for _ in range(201)]

#가로 설정
for i in range(1, 201):
    dp[1][i] = 1
    dp[2][i] = i+1

#세로 설정 n이 1일때
for j in range(2, 201):
    dp[j][1] = j
    for i in range(2,201):
        dp[j][i] = (dp[j][i-1] + dp[j-1][i])%1000000000


print(dp[k][n])