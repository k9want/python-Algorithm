"""
누적 합 형태로 쭈욱 전값을 이용한다. dp방식
"""
import sys
input = sys.stdin.readline
INF = 1000001

dp = [0] * INF

#누적합을 위한
dp_sum = [0] * INF

for i in range(1, INF):
    j = 1
    while i * j < INF:
        dp[i * j] += i
        j += 1
    dp_sum[i] = dp_sum[i-1] + dp[i]


for _ in range(int(input())):
    n = int(input())
    print(dp_sum[n])
