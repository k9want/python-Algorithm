"""
전에 풀었던 것과 똑같은 문제
dp = dp[i-1] + dp[i-2]
"""
def solution(n):
    answer = 0
    d = [0] * (n+1)
    d[1] = 1
    d[2] = 2
    for i in range(3, n+1):
        d[i] = (d[i-1] + d[i-2]) % 1000000007
    answer = d[n]
    return answer