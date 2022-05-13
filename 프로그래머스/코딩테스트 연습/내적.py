"""
바로가능
문제에 맞게 코드작성하면 된다.
"""


def solution(a, b):
    answer = 0

    for i in range(len(a)):
        answer += (a[i] * b[i])

    return answer