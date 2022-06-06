from collections import deque

n, m = map(int,input().split())
graph = []

dy = [1,-1,0,0]
dx = [0,0,-1,1]

for _ in range(n):
    graph.append(list(map(int,input())))

visited = [[0] * m for _ in range(n)]
#print(visited)


q = deque()
q.append((0,0))
while q:
    y, x = q.popleft()
    visited[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1 and visited[ny][nx] == 0:
            graph[ny][nx] = graph[y][x] + 1
            q.append((ny, nx))

print(graph[-1][-1])