# stk을 인덱스로 해서 푸는 문제
# result = [-1] * n 기본적으로 default를 설정하고 푸는 것도 하나의 방법!!

n = int(input())
input_data = list(map(int, input().split()))
stk = []
result = [-1] * n


for i in range(n):
    while stk and input_data[stk[-1]] < input_data[i]:
        result[stk.pop()] = input_data[i]
    stk.append(i)


print(*result)