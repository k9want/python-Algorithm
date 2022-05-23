"""
처음 생각난 중복순열로 풀기
"""
from itertools import combinations_with_replacement
from collections import Counter


def solution(n, info):
    max_diff = 0
    max_cnt = {}

    for c in combinations_with_replacement(range(11), n):
        cnt = Counter(c)
        s1, s2 = 0, 0
        for i in range(1, 11):
            if info[10 - i] < cnt[i]:
                s1 += i
            elif info[10 - i] > 0:
                s2 += i

        diff = s1 - s2
        if diff > max_diff:
            max_cnt = cnt
            max_diff = diff

    if max_diff > 0:
        answer = [0] * 11
        for n in max_cnt:
            answer[10 - n] = max_cnt[n]
        return answer
    else:
        return [-1]

    return answer