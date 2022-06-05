t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    money = int(input())
    dp = [0 for _ in range(money+1)]
    dp[0] = 1

    for c in coins:
        for i in range(1, money+1):
            if i-c >=0:
                dp[i] += dp[i-c]

    print(dp[money])