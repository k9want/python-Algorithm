"""
1. 아아디어
- 2중 for문 => 값이 1이면 방문 , 단 재방문은 x => BFS
- BFS 돌면서 그림 개수 + 1 최대값 갱신

2. 시간복잡도
BFS - : O(V+E)
V = m * n
E = 4v
5 * 500 * 500 => 250000 백만가능

3. 자료구조
- 그래프 행렬  int [][]
- 방문 bool[][]
-queue (bfs)
"""
import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def bfs(y,x):
    rs = 1
    q = deque()
    q.append((y,x))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1 and visited[ny][nx] == False:
                    rs +=1
                    visited[ny][nx] = True
                    q.append((ny, nx))

    return rs



cnt = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if graph[j][i] == 1 and visited[j][i] == False:
            visited[j][i] = True
            cnt += 1
            maxv = max(maxv, bfs(j,i))

print(cnt)
print(maxv)
