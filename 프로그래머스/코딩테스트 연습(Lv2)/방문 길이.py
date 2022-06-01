"""
길은 양방향
set에 (시작 y, x , 끝y, x)와 (끝y, x 시작 y, x) 두개를 add해준다.
총 네가지 방향 U D L R을 사전형으로 넣고
for문으로 방향의 인덱스 값을 뽑아서 그것을 이용한다.
"""


def solution(dirs):
    # U D R L
    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]

    direction = {'U': 0, 'D': 1, 'R': 2, 'L': 3}

    visited = set()
    answer = 0

    y, x = 5, 5
    for d in dirs:
        i = direction[d]
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny <= 10 and 0 <= nx <= 10:
            if (y, x, ny, nx) not in visited:
                # 길은 왼쪽 -> 오른쪽 , 왼쪽 <- 오른쪽 둘다 가능하니까
                visited.add((y, x, ny, nx))
                visited.add((ny, nx, y, x))
                answer += 1
            y, x = ny, nx
        else:
            continue

    return answer