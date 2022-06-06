"""
완탐처럼 돌면서
1이면 bfs 실행 매번 전결과에 1을 더해서 각각 따로 cnt+1이 되도록 했다.
마지막 결과들을 len으로 개수를 구하고
sort()후 차례대로 출력

dfs로는 재귀 사용
이 때도 완탐처럼 전부 다 돌면서 방문안했고 1이면 dfs탐색을 하도록 실행
"""
from collections import deque
n = int(input())

#그래프 초기화
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

#방문체크 초기화
visited = [[0] * n for _ in range(n)]

#탐색을 위해 네가지방향
dy = [-1,1,0,0]
dx = [0,0,-1,1]

# bfs
q = deque()

result = []

for j in range(n):
    for i in range(n):
        if graph[j][i] == 1 and visited[j][i] == 0:
            cnt = 0
            q.append((j,i))
            while q:
                y, x = q.popleft()
                visited[y][x] = 1
                cnt += 1
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == 1 and visited[ny][nx] == 0:
                        graph[ny][nx] = graph[y][x] +1
                        q.append((ny, nx))

            result.append(cnt)
print(len(result))
result.sort()
for res in result:
    print(res)

#dfs로 우선
# def dfs(y,x, cnt):
#     graph[y][x] = 0
#     for d in range(4):
#         ny = y + dy[d]
#         nx = x + dx[d]
#
#         if 0<=ny<n and 0<= nx < n and visited[ny][nx] == 0 and graph[ny][nx] == 1:
#             cnt = dfs(ny, nx, cnt+1)
#     return cnt
#
#
# houses = []
# cnt = 1
# for j in range(n):
#     for i in range(n):
#         if graph[j][i] == 1 and visited[j][i] == 0:
#             houses.append(dfs(j, i, cnt))
# print(len(houses))
# houses.sort()
# for h in houses:
#     print(h)