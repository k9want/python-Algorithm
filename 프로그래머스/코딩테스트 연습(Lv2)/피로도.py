"""
던전 정렬 최소필요 높은순 소모 낮은순으로 //아닌듯
완탐 tip은 순열을 쓰고 제일 많이 간 값을 출력하는 것으로 해결
"""
from itertools import permutations


def solution(k, dungeons):
    answer = -1

    data = list(permutations(dungeons, len(dungeons)))

    for d in data:
        p = k
        result = 0
        for i in range(len(d)):
            if p < d[i][0]:
                break
            p -= d[i][1]
            result += 1
        answer = max(answer, result)

    return answer