"""
int(___ , 해당 진법)
3진법을 10진법으로 바꾸고 싶다면?
int( ___, 3) <-- 이렇게
"""

from collections import deque

def solution(n):
    result = deque([])
    answer = 0

    while True:
        if n < 3:
            result.appendleft(str(n % 3))
            break
        result.appendleft(str(n % 3))
        print(n % 3)
        n = n // 3

    # str_answer = int(''.join(list(result)))

    for i in range(len(result)):
        x = 3 ** i
        answer += int(result[i]) * x

    return answer