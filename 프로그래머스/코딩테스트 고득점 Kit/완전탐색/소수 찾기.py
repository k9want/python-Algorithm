"""
순열로 뽑고
숫자로 만든다음
set으로 중복제거하고
소수 판별 체크
"""
import math
from itertools import permutations


# 소수판별 체크
def check(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0

    n = []
    num = []
    for i in range(1, len(numbers) + 1):
        n.extend(permutations(numbers, i))
        result = [int(''.join(i)) for i in n]

    for i in set(result):
        if check(i):
            answer += 1

    return answer