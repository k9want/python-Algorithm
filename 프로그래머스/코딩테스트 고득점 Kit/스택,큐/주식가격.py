"""
문제를 이해하는게 힘들었던 문제
"""
from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []

    while queue:
        p = queue.popleft()
        n = 0
        for q in queue:
            n += 1
            if p > q:
                break
        answer.append(n)
    return answer