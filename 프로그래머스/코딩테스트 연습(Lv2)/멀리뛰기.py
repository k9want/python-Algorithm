"""
dp 문제
주의할 점은 만약 n < 3 이때의 예외처리를 해줄것!!!
n이 1인데
dp[2]는 조회가 불가능!!!
"""
def solution(n):
    jump = [1, 2]

    dp = [0] * (n + 1)
    if n < 3:
        return n

    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    answer = dp[n] % 1234567
    return answer