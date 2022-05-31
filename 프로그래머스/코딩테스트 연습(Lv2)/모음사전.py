"""
중복 순열을 이용한 문제
from itertools import product
 중복순열은 product(iterable, repeat= '')
 repeat을 사용한다.
"""

from itertools import product


def solution(word):
    words = []
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(c))
    words.sort()
    # print(words)

    return words.index(word) + 1