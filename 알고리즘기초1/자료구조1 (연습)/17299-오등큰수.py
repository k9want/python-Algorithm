# n = int(input())
# data = list(map(int, input().split()))
# result = [-1] * n
# stk = []
#
# # 숫자는 1부터 시작하니까 0을 넣어준다.
# # 밑에 부분 때문에 시간초과
# count = [0]
# set_data = set(data)
# for s in set_data:
#     count.append(data.count(s))
#
# for i in range(n):
#     while stk and count[data[stk[-1]]] < count[data[i]]:
#         result[stk.pop()] = data[i]
#     stk.append(i)
#
# print(*result)

# -----------------------------
# # 중복원소 파악하기 try-except버전
# import sys
# input = sys.stdin.readline
# n = int(input())
# data = list(map(int, input().split()))
# result = [-1] * n
# stk = []
#
# # 숫자는 1부터 시작하니까 0을 넣어준다.
# count = {}
# for i in data:
#     try: count[i] +=1
#     except: count[i] = 1
#
#
# for i in range(n):
#     while stk and count[data[stk[-1]]] < count[data[i]]:
#         result[stk.pop()] = data[i]
#     stk.append(i)
#
# print(*result)

# -----------------------------
# 중복원소 파악하기 Counter
# Counter가 짱~!
import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
result = [-1] * n
stk = []

count = Counter(data)

for i in range(n):
    while stk and count[data[stk[-1]]] < count[data[i]]:
        result[stk.pop()] = data[i]
    stk.append(i)

print(*result)
