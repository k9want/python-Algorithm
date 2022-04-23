"""
시간복잡도
- DFS : O(V+E)
- V E : N^2, 4N^2
- V + E : 5N^2 => N^2 => 625

"""
import sys
input = sys.stdin.readline
n = int(input())

graph = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False] * n for _ in range(n)]
res = 0
result = []

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y, x):
    global res
    res += 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<n and 0<=nx<n:
            if chk[ny][nx] == False and graph[ny][nx] == 1:
                chk[ny][nx] = True
                dfs(ny, nx)


for j in range(n):
    for i in range(n):
        if graph[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            res = 0
            dfs(j, i)
            result.append(res)


result.sort()
print(len(result))
for r in result:
    print(r)