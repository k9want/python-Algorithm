"""
2중for문을 사용한 완전탐색
"""


def solution(n):
    answer = 0

    for j in range(1, n + 1):
        result = 0
        for i in range(j, n + 1):
            result += i
            if result == n:
                answer += 1
                break
            elif result > n:
                break

    return answer