"""
dfs로 푸는 코드
"""
def dfs(numbers, target, i):
    answer = 0
    if i == len(numbers):
        # print(numbers)
        if sum(numbers) == target:
            return 1
        else:
            return 0

    else:
        answer += dfs(numbers, target, i + 1)
        numbers[i] *= -1
        answer += dfs(numbers, target, i + 1)
        return answer


def solution(numbers, target):
    answer = dfs(numbers, target, 0)

    return answer


"""
bfs로 푼 코드
"""
from collections import deque


def solution(numbers, target):
    answer = 0

    q = deque()

    n = len(numbers)
    q.append([-numbers[0], 0])
    q.append([numbers[0], 0])

    while q:
        num, i = q.popleft()
        if i + 1 == n:
            if num == target:
                answer += 1

        else:
            i += 1
            q.append([num - numbers[i], i])
            q.append([num + numbers[i], i])

    return answer