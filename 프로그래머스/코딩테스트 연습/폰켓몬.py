"""
간단하게 생각해도 된다.
"""


def solution(nums):
    set_nums = set(nums)
    answer = 0

    n = len(nums)
    if (n // 2) > len(set_nums):
        answer = len(set_nums)
    else:
        answer = (n // 2)

    return answer