"""
뱀의 위치를 board에서 -1로 표현
뱀의 몸통을 q에 넣고
뱀이 부딪치는지 확인하기 위해 -1이면 break 아니면 벽에 부딪치는지를 체크할 것
후에
사과가 없다면 q.append()하고 나서 꼬리부분을 빼주는 q.popleft()
사과 있다면 q.append()하기
"""
from collections import deque
n = int(input())
board = [[0] * (n+1) for _ in range(n+1)]
k = int(input())
for _ in range(k):
    y, x = map(int, input().split())
    board[y][x] = 1
l_data = []
l = int(input())
for _ in range(l):
    l_data.append(list(input().split()))
#뱀은 처음에 오른쪽 북 동 남 서

dy = [-1,0,1,0]
dx = [0,1,0,-1]
d = 1
def turn(direction):
    global d
    if direction == 'D':
        d += 1
        if d > 3:
            d = 0
    elif direction == 'L':
        d -= 1
        if d < 0:
            d = 3

#뱀의 몸



def simulation():
    y, x = 1, 1
    board[y][x] = -1
    global d
    index = 0
    time = 0
    q = deque()
    q.append((y, x))
    while True:
        ny = y + dy[d]
        nx = x + dx[d]
        if 1 <= ny <= n and 1 <= nx <= n and board[ny][nx] != -1:
            #사과 없다면??
            if board[ny][nx] == 0:
                board[ny][nx] = -1
                #머리는 큐에 넣고
                q.append((ny, nx))
                # 꼬리는 뺀다
                tail_y, tail_x = q.popleft()
                board[tail_y][tail_x] = 0
            #사과 있다면??
            if board[ny][nx] == 1:
                board[ny][nx] = -1
                q.append((ny, nx))
        else:
            time += 1
            break
        y, x = ny, nx
        time += 1
        if index < l and time == int(l_data[index][0]):
            turn(l_data[index][1])
            index += 1
    return time

print(simulation())
