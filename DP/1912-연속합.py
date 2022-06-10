# n = int(input())
# data = list(map(int, input().split()))
# dp = [0] * n
#
# dp[0] = data[0]
#
# for i in range(1, n+1):
#     dp[i] = max(data[i-1], data[i-1] + dp[i])
#
# print(max(dp))


n = int(input())

arr = list(map(int, input().split()))
dp = [0] * len(arr)
dp[0] = arr[0]

for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i-1] + arr[i])

print(max(dp))