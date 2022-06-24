"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

답:
3
"""


# n, m = map(int, input().split())
#
# x, y, direction = list(map(int,input().split()))
#
# data = [list(map(int, input().split())) for _ in range(n)]
#
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
#
# #방문처리
# d =[[0] * m for _ in range(n)]
# d[x][y] = 1
#
# def turn_left():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3
#
# cnt = 1
# turn_time = 0
#
# while True:
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#
#     if d[ny][nx] == 0 and data[nx][ny] == 0:
#         d[ny][nx] = 1
#         x = nx
#         y = ny
#         cnt += 1
#         turn_time = 0
#         continue
#
#     else:
#         turn_time += 1
#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#
#         if data[ny][nx] == 0:
#             x = nx
#             y = ny
#         else:
#             break
#         turn_time = 0
#
# print(cnt)

n, m = map(int, input().split())
y, x, d = map(int, input().split())
visited = [[0] * m for _ in range(n)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

visited[y][x] = 1

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3


cnt = 1
turn_time = 0
while True:
    #우선 왼쪽 방향으로 회전
    turn_left()
    ny = y + dy[d]
    nx = x + dx[d]
    if visited[ny][nx] == 0 and data[ny][nx] == 0:
        visited[ny][nx]= 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        ny = y - dy[d]
        nx = x - dx[d]
        if data[ny][nx] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(cnt)



#print(data)

"""
4 4 
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""

