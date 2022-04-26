"""
동전별로 경우의 수를 고려할 것
한번에 금액의 경우의수를 구하는 것이 아님 이로 점화식을 구하는데 오래걸렷음
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0] * 10001
dp[0] = 1

for c in coins:
    for i in range(c, m+1):
        dp[i] = dp[i] + dp[i-c]

print(dp[m])