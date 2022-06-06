"""
기존 숨바꼭질에 경로를 추가로 출력해야한다.
path 배열을 만들고
path[다음칸] = 현재칸 이렇게 저장을 한뒤
나중에 k에 도달했을 때 역으로 이전칸 = path[지금칸]
이렇게 해서 이전칸이 n일때까지 result배열에 따로 저장한다.
n을 추가하고 reverse로 바꾸고 출력


"""
from collections import deque
n, k = map(int, input().split())
INF = 100001

visited = [0] * INF
path = [0] * INF
result = []
q = deque()
q.append(n)

while q:
    x = q.popleft()

    if x == k:
        #역순으로 n까지 꺼내기
        while x != n:
            result.append(path[x])
            #x = 18(path[17]) 10 = path[18]
            x = path[x]
        break
    for nx in (x-1, x+1, x*2):
        if 0<= nx < INF and visited[nx] == 0:
            visited[nx] = visited[x]+1
            #path[다음좌표] = 현재좌표
            #ex path[10] = 5 path[18] = 10 path[17] = 18
            path[nx] = x
            q.append(nx)
result.reverse()
result.append(k)
print(visited[k])
print(*result)
