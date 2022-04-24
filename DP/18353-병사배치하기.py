"""
가장 긴 증가하는 부분 수열 유형이라고 한다.
N^2
"""
n = int(input())
data = list(map(int, input().split()))
data.reverse()

dp = [1] * n

for i in range(n):
    for j in range(0, i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))
