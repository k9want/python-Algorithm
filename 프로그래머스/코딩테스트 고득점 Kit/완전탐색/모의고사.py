"""
문제수가 최대 10000문제이므로
각각의 리스트를 최대 10000개 만들고 전부 탐색을 했다.
최댓값을 뽑고 각각의 맞은 개수와 비교해서 answer에 넣는것으로 코드를 작성했다.
"""
def solution(answers):
    a = [1, 2, 3, 4, 5] * 2000
    b = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    answer = []
    r1 = 0
    r2 = 0
    r3 = 0

    for i in range(len(answers)):
        if answers[i] == a[i]:
            r1 += 1
        if answers[i] == b[i]:
            r2 += 1
        if answers[i] == c[i]:
            r3 += 1

    v = max(r1, r2, r3)

    if r1 == v:
        answer.append(1)
    if r2 == v:
        answer.append(2)
    if r3 == v:
        answer.append(3)

    return answer