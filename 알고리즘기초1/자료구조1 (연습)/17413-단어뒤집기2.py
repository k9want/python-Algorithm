# import sys
# from collections import deque
#
# dq = deque()
# stk = []
# input_data = sys.stdin.readline().rstrip()
# for i in range(len(input_data)):
#     if input_data[i] == ' ':
#         while stk:
#             if not stk:
#                 break
#             else:
#                 print(stk.pop(), end='')
#
#     if input_data[i] == '<':
#         while stk:
#             if not stk:
#                 break
#             else:
#                 print(stk.pop(), end='')
#         print('<', end='')
#         while True:
#             i += 1
#             if input_data[i] == '>':
#                 print('>', end='')
#                 i += 1
#                 break
#             else:
#                 print(input_data[i], end='')
#     else:
#         stk.append(input_data[i])

#--------------------
# 다시 시도
# 태그 안과 밖에서의 순서차이가 있다.
# 따라서 태그 안인지 밖인지 상태를 알려주는 변수를 하나 추가해서 문제 해결

import sys
from collections import deque

dq = deque()
stk = []
result = ''
#태그 안일때는 True, 밖일때는 False
tag = False

input_data = sys.stdin.readline().rstrip()
for i in input_data:
    if i == '<':
        while stk:
            result += stk.pop()
        dq.append(i)
        tag = True
    elif i == '>':
        dq.append(i)
        tag = False
        while dq:
            result += dq.popleft()
    elif i == ' ':
        if tag:
            dq.append(i)
        else:
            while stk:
                result += stk.pop()
            result += ' '

    else:
        if tag:
            dq.append(i)
        else:
            stk.append(i)

while stk:
    result += stk.pop()

print(result)

