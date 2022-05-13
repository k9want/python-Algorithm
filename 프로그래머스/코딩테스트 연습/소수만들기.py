"""
소수 판별은 에라토스테네스의 체를 이용한다.
암기~~하자
"""
from itertools import combinations

def is_prime_number(num):
    if num == 0 or num == 1:
        return False
    else:
        for n in range(2, (num // 2) + 1):
            if num % n == 0:
                return False

        return True

def solution(nums):
    answer = 0
    result = []

    for c in list(combinations(nums, 3)):
        result.append(sum(c))

    for rs in result:
        if is_prime_number(rs):
            answer += 1

    return answer