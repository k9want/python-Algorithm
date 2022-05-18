"""
중복제거는 set으로
"""

from itertools import combinations


def solution(numbers):
    result = list(combinations(numbers, 2))
    answer = []
    for rs in result:
        answer.append(sum(rs))

    ans = sorted(list(set(answer)))
    return ans