import sys
input = sys.stdin.readline
"""
마지막에 끝나는 수를 기준으로 몇개인지 저장해둔다.
"""
t = int(input())
data =[]
for _ in range(t):
    data.append(int(input()))

INF = 100001
dp = [[0 for _ in range(3)] for _ in range(INF)]
dp[1] = [1,0,0]
dp[2] = [0,1,0]
dp[3] = [1,1,1]

for i in range(4, INF):
    # dp[i] = [ dp[i-1][2] + dp[i-1][3],
    #           dp[i-2][1] + dp[i-2][3],
    #           dp[i-3][2] + dp[i-3][1]
    #         ]
    dp[i] = [ dp[i-1][1] % 1000000009 + dp[i-1][2] % 1000000009,
              dp[i-2][0]% 1000000009 + dp[i-2][2]% 1000000009,
              dp[i-3][1]% 1000000009 + dp[i-3][0]% 1000000009
            ]

for d in data:
    print(sum(dp[d]) % 1000000009)