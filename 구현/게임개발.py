n, m = map(int, input().split())

x, y, direction = list(map(int,input().split()))

data = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

#방문처리
d =[[0] * m for _ in range(n)]
d[x][y] = 1

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

cnt = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[ny][nx] == 0 and data[nx][ny] == 0:
        d[ny][nx] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue

    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if data[ny][nx] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(cnt)

