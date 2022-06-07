"""
이 문제의 핵심
n * 2 즉 순간이동을 할 때는 시간이 0초 그대로이다.
따라서 이 부분을 우선순위로 둘것!!!
q.appendleft로 우선순위를 둔다.
"""
from collections import deque
n, k = map(int,input().split())
INF = 100001
graph = [0] * INF
visited = [0] * INF
q = deque()
q.append(n)

while q:
    x = q.popleft()
    visited[x] = 1
    if x == k:
        break
    for nx in (x-1, x+1, x*2):
        if 0 <= nx < INF and graph[nx] == 0 and visited[nx] == 0:
            if nx == x * 2:
                graph[nx] = graph[x]
                q.appendleft(nx)
            else:
                graph[nx] = graph[x] + 1
                q.append(nx)
            #print(graph)
print(graph[k])

