from collections import deque


def solution(n, edge):
    answer = 0

    # 그래프 셋팅
    graph = [[] for _ in range(n + 1)]
    dist = [-1] * (n + 1)

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    q = deque([1])
    dist[1] = 0

    # bfs 시작
    while q:
        v = q.popleft()
        for i in graph[v]:
            if dist[i] == -1:
                q.append(i)
                dist[i] = dist[v] + 1

    for d in dist:
        if d == max(dist):
            answer += 1

    return answer