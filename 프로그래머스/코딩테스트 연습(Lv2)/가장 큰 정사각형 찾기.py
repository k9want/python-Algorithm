"""
가능할 수 있는 한변의 최대 길이를 찾고 곱한다.
이 때 한변의 최대 길이를 찾는 방법은 4개 중 가장 작은 값에 +1을 할 것

"""

def solution(board):
    answer = 0

    y = len(board)
    x = len(board[0])

    # dp 셋팅
    dp = [[0] * x for _ in range(y)]
    dp[0] = board[0]
    for i in range(1, y):
        dp[i][0] = board[i][0]

    # 2중 for문으로 연산
    for j in range(1, y):
        for i in range(1, x):
            if board[j][i] == 1:
                dp[j][i] = min(dp[j - 1][i - 1], dp[j - 1][i], dp[j][i - 1]) + 1

    for i in range(y):
        tmp = max(dp[i])
        answer = max(answer, tmp)

    return answer * answer