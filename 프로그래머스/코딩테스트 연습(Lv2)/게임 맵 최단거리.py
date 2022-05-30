"""
bfs 문제
"""

#시간초과 난 코드
"""
from collections import deque
def solution(maps):
    
    n = len(maps)
    m = len(maps[0])
    
    answer = 0
    
    dy = [1,-1,0,0]
    dx = [0,0,-1,1]
    
    #1이면 갈 수 있고 0이면 못간다. 
    visited =[[True] * m for _ in range(n)]
    for j in range(n):
        for i in range(m):
            if maps[j][i]:
                visited[j][i] = False
    
    
    q = deque()
    
    q.append((0, 0))
    while q:
        y, x = q.popleft()
        visited[y][x] = True
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                maps[ny][nx] = maps[y][x] + 1
                q.append((ny, nx))    
                
    answer = maps[-1][-1]
    
    if visited[-1][-1]:
        return answer
    
    return -1
"""


#꼼꼼하게 코딩하자...
#if matrix[ny][nx] == -1 빼먹음 의미없는 값들이 q에 들어갔다.
from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    answer = 0

    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    # 1이면 갈 수 있고 0이면 못간다. visited말고 maps를 이용

    matrix = [[-1 for _ in range(m)] for _ in range(n)]
    # print(matrix)

    q = deque()
    matrix[0][0] = 1

    q.append((0, 0))
    while q:
        y, x = q.popleft()
        maps[y][x] = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] and matrix[ny][nx] == -1:
                matrix[ny][nx] = matrix[y][x] + 1
                q.append((ny, nx))

    answer = matrix[-1][-1]

    return answer