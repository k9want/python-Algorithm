"""
1. 최대 30까지 이기 때문에 완전탐색 가능
2. y,x y,x+1 가 일치하는지? 일치하면 y+1,x y+1,x+1과도 일치하는지?
3. 일치하면 터뜨리고 0 으로 입력
    -이때 중복제거
4. 아래로 내리기 <-- 각각의 x, y를 저장해놓고 정렬한뒤 해당 y의 역순으로 반복적으로 위로 올린다.!!!

"""


def solution(m, n, board):
    answer = 0
    new_board = []
    for b in board:
        new_board.append(list(b))
    board = new_board
    # print(board)

    bomb = []

    while True:
        """
        for b in board:
            print(b)
        print('----')
        """

        for j in range(m - 1):
            for i in range(n - 1):
                if board[j][i] == '0':
                    continue
                if board[j][i] == board[j][i + 1]:
                    if board[j + 1][i] == board[j + 1][i + 1] == board[j][i]:
                        bomb.append((j, i))
                        bomb.append((j, i + 1))
                        bomb.append((j + 1, i))
                        bomb.append((j + 1, i + 1))

        if len(bomb) != 0:
            # 폭탄제거
            bomb = list(set(bomb))
            answer += len(bomb)
            for b in bomb:
                board[b[0]][b[1]] = '0'

            # 위에 블록 내려오게 하기

            bomb.sort(reverse=True)
            # print(bomb)

            for i in range(len(bomb)):
                y, x = bomb.pop()
                for a in range(y, 0, -1):
                    board[a][x], board[a - 1][x] = board[a - 1][x], board[a][x]





        else:
            break

    return answer