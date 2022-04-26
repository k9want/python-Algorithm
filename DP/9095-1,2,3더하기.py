"""
아이디어 바로전 +1 전전 +2 전전전 +3까지의 경우의 수를 생각
결국엔 현재 구하는 인덱스의 3번째 전까지들의 경우의 수를 더하는 것
앞의 결과를 이용하는 DP문제


"""

for _ in range(int(input())):


    n = int(input())

    dp = [0] * 11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n])