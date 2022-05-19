"""
bfs()유형
P가 2이하이면 false를
O가 1이면 한번더 탐색을 하도록 bfs 코드 작성

시작점은 각각의 P이다.
한번더 풀어볼것!!
"""

from collections import deque


def bfs(y, x, d, place):
    q = deque([])
    visited = [[False] * 5 for _ in range(5)]
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    q.append([y, x, d])
    while q:
        y, x, d = q.popleft()
        visited[y][x] = True
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            nd = d + 1
            if 0 <= ny < 5 and 0 <= nx < 5 and visited[ny][nx] == False:
                visited[ny][nx] = True

                if place[ny][nx] == 'P':
                    if nd <= 2:
                        return False

                elif place[ny][nx] == 'O':
                    if nd == 1:
                        q.append([ny, nx, nd])
    return True


def solution(places):
    answer = []

    for place in places:
        result = 1

        for j in range(len(place)):
            for i in range(len(place)):
                if place[j][i] == 'P':
                    check = bfs(j, i, 0, place)
                    if not check:
                        result = 0
        answer.append(result)

    return answer