from collections import deque


def solution(priorities, location):
    # location에 있는 숫자만 특별한 표시를 위해 1로 표시 나머지는 0으로해서 튜플로 리스트 원소를 바꿈
    q = deque([])
    answer = 1

    for i in range(len(priorities)):
        if i == location:
            q.append((priorities[i], 1))
        else:
            q.append((priorities[i], 0))

    while q:
        p, i = q.popleft()
        max_value = 0
        for j in range(len(q)):
            if max_value <= q[j][0]:
                max_value = q[j][0]

        if p >= max_value:
            if i == 1:
                break
            else:
                answer += 1
        else:
            q.append((p, i))

    return answer