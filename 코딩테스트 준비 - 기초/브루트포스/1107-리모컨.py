# 버튼으로 채널 이동이 가능한지 불가능한지 판별하여 모든 수를 판별한다.
# 버튼이 되는지 안되는지 우선 o x로 판별 그 후에 + - 로 이동한다.
# 모든 수를 다 본다는 것을 잊지 말자

n = int(input())
m = int(input())
broken = [False] * 10
if m > 0:
    a = list(map(int, input().split()))
else:
    a = []
for x in a:
    broken[x] = True

def possible(c):
    if c == 0:
        if broken[0]:
            return 0
        else:
            return 1
    l = 0
    while c > 0:
        if broken[c % 10]:
            return 0
        l += 1
        c //= 10
    return l

ans = abs(n - 100)
for i in range(0, 1000000 + 1):
    c = i
    l = possible(c)
    if l > 0:
        press = abs(c - n)
        if ans > l + press:
            ans = l + press
print(ans)
