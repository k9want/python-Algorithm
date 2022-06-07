"""
핵심은!! 0 -> 0을 1순위 appendleft
벽을 부수는 행동을 2순위로 둔다. append
"""
from collections import deque
n, m = map(int, input().split())
graph = []
data = [[-1]*n for _ in range(m)]

for _ in range(m):
    graph.append(list(map(int, input())))
#print(graph)
#print(data)
dy = [-1,1,0,0]
dx = [0,0,-1,1]

q = deque()
q.append((0,0))
while q:
    y, x = q.popleft()
    data[0][0] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < m and 0 <= nx < n and data[ny][nx] == -1:
            # 0 -> 0 은 우선순위 !!
            if graph[ny][nx] == 0:
                data[ny][nx] = data[y][x]
                q.appendleft((ny, nx))
            else:
                data[ny][nx] = data[y][x] + 1
                q.append((ny, nx))

print(data[m-1][n-1])


#미로 밖 x

#음 검사 안되면 하나 안되면 두개 안되면 세개 점차 늘린다.