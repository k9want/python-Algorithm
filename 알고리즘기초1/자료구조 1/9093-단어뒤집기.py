# 풀이 1 stack으로
# n = int(input())
#
# for _ in range(n):
#     stk = []
#     input_data = input()
#     input_data += ' '
#     # print(input_data)
#     for i in input_data:
#
#         if i != ' ':
#             stk.append(i)
#         else:
#             while stk:
#                 print(stk.pop(), end='')
#             print(' ', end='')


# 풀이 1-1 sys.stdin.readline().rstrip
# import sys
#
# n = int(input())
#
# for _ in range(n):
#     input = sys.stdin.readline().rstrip
#     stk = []
#     input_data = input()
#     input_data += ' '
#     # print(input_data)
#     for i in input_data:
#
#         if i != ' ':
#             stk.append(i)
#         else:
#             while stk:
#                 print(stk.pop(), end='')
#             print(' ', end='')


# 풀이 2 리스트로 [::-1] 이용
n = int(input())

for i in range(n):
    input_data = input().split()
    for id in input_data:
        print(id[::-1], end=' ')




