# stk으로 생각
# 값 출력할 result 고려
# 현재값과 비교할 변수를 만드는 부분

stk = []
result = []
i = 0
x = True

for _ in range(int(input())):
    n = int(input())

    while i < n:
        i += 1
        stk.append(i)
        result.append('+')

    if (stk[-1] == n):
        stk.pop()
        result.append('-')
    else:
        x = False
        print('NO')
        break

if x:
    for r in result:
        print(r)





