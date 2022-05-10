#queue를 사용
from collections import deque


def solution(progresses, speeds):
    answer = []
    p = deque(progresses)
    s = deque(speeds)

    while p:
        cnt = 0
        for i in range(len(s)):
            p[i] += s[i]
        for j in range(len(p)):
            if p[0] >= 100:
                p.popleft()
                s.popleft()
                cnt += 1
        if cnt > 0:
            answer.append(cnt)

    return answer