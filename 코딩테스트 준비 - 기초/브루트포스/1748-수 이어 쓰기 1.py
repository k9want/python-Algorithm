# 자릿수별로 나눠서
# end = start * 10 -1 => 9 = 10 - 1 // 99 = 100 - 1
n = int(input())
ans = 0
start = 1
length = 1
while start <= n:
    end = start * 10 - 1
    if end > n:
        end = n
    ans += (end - start + 1) * length
    start *= 10
    length += 1
print(ans)
