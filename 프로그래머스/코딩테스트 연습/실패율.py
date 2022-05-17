"""
문제에 맞게 구현하는데
리스트로 했던 나의 풀이보단 다른 사람의 풀이를 보니 사전형을 이용한 풀이도 좋아보였다.
각각의 스테이지별로 유저들을 구해서 나누고 결과를 정렬후 출력하면 되는 문제 
"""
def solution(N, stages):
    answer = []
    user = len(stages)
    result = []
    for i in range(1, N + 1):
        cnt = stages.count(i)
        if cnt == 0:
            result.append((0, i))
        else:
            result.append((cnt / user, i))
        user -= cnt

    result.sort(key=lambda x: (-x[0], x[1]))
    print(result)
    for rs in result:
        answer.append(rs[1])

    return answer