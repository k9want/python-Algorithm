"""
yellow와 brown 관계를 우선 찾기
brown = yellow의 가로 * 2 + yellow의 세로 * 2 + 4
"""
def solution(brown, yellow):
    answer = []

    x = 0
    y = 0

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            x = int(yellow / i)
            y = i
            if x * 2 + y * 2 + 4 == brown:
                answer.append(x + 2)
                answer.append(y + 2)

                return sorted(answer, reverse=True)

    return answer