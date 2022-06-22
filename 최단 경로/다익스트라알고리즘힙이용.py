import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start =  int(input())
graph = [[] for i in range(n+1)]
dist = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def solution(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for i in graph[now]:
            print(i)
            cost = d + i[1]

            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

solution(start)

for i in range(1, n+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])


"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""

