"""
아이디어 - 기존값을 사용한다. DP인지 고려

경우의 수가 매번 다르기 때문에 전부 고려해서 비교한다.
dp = []
result = []만들고 최댓값 비교

"""

n = int(input())
t = [0]
p = [0]
dp = [0] * (n+2)
result = 0

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for j in range(1, n+2):
    for i in range(1, j):
        # 일하고 온거
        if i + t[i] == j:
            dp[j] = max(dp[j], dp[i] + p[i])
        # 일 안하고 온거
        dp[j] = max(dp[i], dp[j])

    result = max(result, dp[j])

print(result)

