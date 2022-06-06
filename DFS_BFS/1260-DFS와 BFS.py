n,m,v = map(int,input().split())

graph = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    y, x = map(int,input().split())
    graph[y][x], graph[x][y] = 1, 1

#방문체크용
visited_b = [0] * (n+1)
visited_d = [0] * (n+1)

#dfs
def dfs(v):
    #우선 방문체크
    visited_d[v] = 1
    print(v, end =' ')
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited_d[i] == 0:
            dfs(i)

#bfs
def bfs(v):
    q = [v]
    visited_b[v] = 1
    while q:
        v = q.pop(0)
        print(v, end =' ')
        for i in range(1, n+1):
            if visited_b[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited_b[i] = 1
dfs(v)
print()
bfs(v)