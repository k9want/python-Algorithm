"""
핵심은 자물쇠를 3배로 해서 전부 탐색하기 수월하게 하고
매법 각각의 방향으로 회전하면서!!
자물쇠에 열쇠를 끼워본다.
끼워보고 안 맞다면 원상복귀 시키는 것까지 중요!!!

"""


def rotate_90(arr):
    y = len(arr)
    x = len(arr[0])
    new_arr = [[0] * y for _ in range(x)]
    for i in range(y):
        for j in range(x):
            new_arr[j][y - i - 1] = arr[i][j]
    return new_arr


def check(new_lock):
    n = len(new_lock) // 3
    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    answer = True

    n = len(lock)
    m = len(key)

    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 중앙 부분에 원래 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    for rotate in range(4):
        key = rotate_90(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check(new_lock) == True:
                    return True

                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False