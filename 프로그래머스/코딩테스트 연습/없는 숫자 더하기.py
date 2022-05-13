"""
바로 풀수있는 간단한 문제
"""


def solution(numbers):
    number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for n in numbers:
        number_list.remove(n)

    answer = (sum(number_list))
    return answer