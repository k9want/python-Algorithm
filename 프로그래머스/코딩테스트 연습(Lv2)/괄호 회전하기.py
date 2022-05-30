"""
check함수 stk사용할 예정 stk으로 해결
for문으로 반복 큐를 쓸 예정
"""
from collections import deque


def check(strr):
    stk = []
    for s in strr:
        if s == ']' or s == ')' or s == '}':
            if not stk:
                return False
            elif (stk[-1] == '[' and s == ']') or (stk[-1] == '(' and s == ')') or (stk[-1] == '{' and s == '}'):
                stk.pop()
        else:
            stk.append(s)
    if not stk:
        return True
    return False


def solution(s):
    answer = 0

    q = deque(s)
    for i in range(len(s)):
        q.rotate(-1)
        if check(q):
            answer += 1

    return answer