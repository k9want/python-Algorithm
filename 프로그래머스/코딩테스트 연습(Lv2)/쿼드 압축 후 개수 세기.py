"""
재귀를 사용
범위 안의 값이 맞으면 해당 범위(n)의 시작점의 값 + 1
틀리다면!! 범위를 나눈다. n // 2 그리고 네 범위에 각각 탐색한다. (재귀 사용)

압축문제
리스트를 실제로 자르는 것보다 인덱스를 구해서 해결하는게 좋다.
"""


def solution(arr):
    answer = [0, 0]
    l = len(arr)

    def recur(y, x, n):
        start = arr[y][x]
        for j in range(y, y + n):
            for i in range(x, x + n):
                if start != arr[j][i]:
                    n = n // 2
                    recur(y, x, n)
                    recur(y, x + n, n)
                    recur(y + n, x, n)
                    recur(y + n, x + n, n)
                    return
        answer[start] += 1

    recur(0, 0, l)

    return answer