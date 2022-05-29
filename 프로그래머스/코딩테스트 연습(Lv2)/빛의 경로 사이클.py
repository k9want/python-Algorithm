"""
dfs, bfs 처럼 방문체크와 방문을 하는 문제
- 각각의 방향마다 방향체크를 위해 visited배열을 3중으로 만든다.
- 회전 방향을 위해 rotate()함수를 만들고 directions의 방향별로 R이면 d = (d+1) % 4처럼
  360 회전을 구현해준다.
- 어렵게 생각하지말고 나눠서 함수로 구현하는 방법도 있다는 것 명심하기
- 참고 https://alreadyusedadress.tistory.com/312?category=1188005
"""


def move(y, x, d):
    global directions, n, m
    dy, dx = directions[d]
    return (y + dy) % n, (x + dx) % m


def rotate(d, direction):
    if direction == 'R':
        d = (d + 1) % 4
    elif direction == 'L':
        d = (d - 1) % 4
    return d


def solution(grid):
    answer = []

    global n, m, directions
    n, m = len(grid), len(grid[0])
    # D L U R
    directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    # 각 방향별로 방문체크
    visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]

    for y in range(n):
        for x in range(m):
            for d in range(4):
                if not visited[y][x][d]:
                    cy, cx, cd = y, x, d
                    cnt = 0
                    while not visited[cy][cx][cd]:
                        visited[cy][cx][cd] = True
                        cnt += 1
                        cy, cx = move(cy, cx, cd)
                        cd = rotate(cd, grid[cy][cx])
                    answer.append(cnt)

    answer.sort()

    return answer