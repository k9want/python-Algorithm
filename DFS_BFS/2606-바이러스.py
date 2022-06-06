"""
visited은 곧 컴퓨터를 의미
graph[a][b] = graph[b][a] = 1 이렇게 두고 탐색을 한다.
컴퓨터의 감염개수를 출력해야한다는 점 유의
따라서 특정 컴퓨터를 방문할 때마다 result +=1을 한다.
"""
from collections import deque
n = int(input())

graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(int(input())):
    a, b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0] * (n+1)


q = deque()
q.append(1)
visited[1] = 1
result = 0
while q:
    y = q.popleft()
    for i in range(1, n+1):
        if graph[y][i] == 1 and visited[i] == 0:
            q.append(i)
            visited[i] = 1
            result += 1

print(result)
