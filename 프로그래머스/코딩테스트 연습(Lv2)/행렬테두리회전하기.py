"""
data[y][x]로 생각 원래하던대로
반복문을 사용
처음 y1-1 x1-1 값은 저장해둔다.
반복문으로 각각 시계방향에 맞는 방향으로 하나씩 이동시킨다. 이동할 값 저장하고 이동할 위치에 있는 곳에 대입하는 방식으로
최솟값도 비교해준다.

"""

def solution(rows, columns, queries):
    answer = []
    data = []
    n = 1
    for _ in range(rows):
        d = []
        for _ in range(columns):
            d.append(n)
            n += 1
        data.append(d)

    # 회전하기 && 최솟값 찾기
    for y1, x1, y2, x2 in queries:

        start = data[y1 - 1][x1 - 1]
        minn = start
        # 왼쪽 위에서부터 시작
        for i in range(y1 - 1, y2 - 1):
            num = data[i + 1][x1 - 1]
            data[i][x1 - 1] = num
            minn = min(minn, num)
        # 밑에 왼쪽부터
        for i in range(x1 - 1, x2 - 1):
            num = data[y2 - 1][i + 1]
            data[y2 - 1][i] = num
            minn = min(minn, num)

        # 오른쪽 밑부터 내리기
        for i in range(y2 - 1, y1 - 1, -1):
            num = data[i - 1][x2 - 1]
            data[i][x2 - 1] = num
            minn = min(minn, num)
        # 위쪽 (오른쪽부터)
        for i in range(x2 - 1, x1 - 1, -1):
            num = data[y1 - 1][i - 1]
            data[y1 - 1][i] = num
            minn = min(minn, num)
        data[y1 - 1][x1] = start
        answer.append(minn)

    return answer