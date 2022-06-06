from collections import deque
n, k = map(int, input().split())
visited = [0] * 100001
q = deque()
q.append(n)
while q:
    x = q.popleft()
    if x == k:
        break
    for nx in (x-1, x+1, x * 2):
        if 0 <= nx < 100001 and visited[nx] == 0:
            visited[nx] = visited[x] + 1
            q.append(nx)
print(visited[k])

