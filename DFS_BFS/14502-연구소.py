"""
세울 벽을 브루트포스 즉 완전탐색으로 전부 탐색을 한다.
벽을 다 세우면 bfs탐색을 한다.
이 결과들의 최댓값을 출력한다.
"""
import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy
dy = [-1,1,0,0]
dx = [0,0,-1,1]
result = 0


#2. 즉 바이러스가 퍼치는 함수
#벽 3개를 세우면 실행되는데
def bfs():
    global result
    #2-1우선은 다음번 탐색을 위해 복사를 해놓는다. deepcopy
    copy_data = deepcopy(data)
    for j in range(y):
        for i in range(x):
            #2-2바이러스를 퍼뜨리기 위해 바이러스들의 좌표를 알아낸다.
            if copy_data[j][i] == 2:
                q.append((j, i))
    #2-3 q 안에있는 바이러스 좌표들로 bfs 탐색을 한다.
    while q:
        qy, qx = q.popleft()
        for d in range(4):
            ny = qy + dy[d]
            nx = qx + dx[d]
            if 0 <= ny < y and 0 <= nx < x:
                if copy_data[ny][nx] == 0:
                    copy_data[ny][nx] = 2
                    q.append((ny, nx))
    #3.탐색한후에 0의 개수를 파악
    cnt = 0
    for cd in copy_data:
        cnt += cd.count(0)
    # 0의 최대값을 result로 출력
    result = max(result, cnt)

# 1. 벽을 세우는 함수로 벽을 하나씩 벽을 세운다.
def wall(w):
    if w == 3:
        #1-1벽이 3개 세워지면 bfs를 실행한다.
        bfs()
        return
    for j in range(y):
        for i in range(x):
            if data[j][i] == 0:
                data[j][i] = 1
                wall(w+1)
                # 그 후 다음을 위해 다시 원상복구를 한다.
                data[j][i] = 0

y, x = map(int,input().split())
data = []
for _ in range(y):
    data.append(list(map(int, input().split())))
q = deque()
wall(0)
print(result)