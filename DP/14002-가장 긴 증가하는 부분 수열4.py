n = int(input())
data = [0]
data.extend(list(map(int, input().split())))

dp = [1] * (n+1)
result = []
for j in range(2, n+1):
    for i in range(1, j):
        if data[i] < data[j]:
            dp[j] = max(dp[j], dp[i]+1)

print(max(dp))
x = max(dp)
for i in range(n, 0, -1):
    if dp[i] == x:
        result.append(data[i])
        x -= 1
result.reverse()
print(*result)