from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
m = int(input())


data = [[]for _ in range(n+1)]
result = [0 for i in range(n+1)]
visited = [0 for i in range(n+1)]

for _ in range(m):
    y, x = map(int, input().split())
    data[y].append(x)
    data[x].append(y)

q = deque()
q.append(a)
visited[a] = 1
while q:
    z = q.popleft()
    for i in data[z]:
        if visited[i] == 0:
            visited[i] = 1
            result[i] = result[z] + 1
            q.append(i)



print(result[b] if result[b] != 0 else -1)

