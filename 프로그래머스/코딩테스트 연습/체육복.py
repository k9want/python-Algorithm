"""
주의 조건 순서를 잘 생각하고 작성할 것
체육복 여벌을 가지고 온 학생이 체육복을 잃어버릴수도 있다는 부분 주의
문제에 설명에 맞게
해당 학생 전후의 번호만을 탐색해서 여벌 체육복을 가지고 있다면 하나 주는 것으로 코드 작성
"""

def solution(n, lost, reserve):
    answer = 0
    data = [1] * (n + 1)

    # 5 531 24 4

    for i in lost:
        data[i] -= 1

    for r in reserve:
        data[r] += 1

    for i in range(1, n + 1):
        if data[i] == 0:
            if i > 1 and data[i - 1] == 2:
                data[i - 1] += 1
                data[i] += 1
            elif i < n and data[i + 1] == 2:
                data[i + 1] += 1
                data[i] += 1

    for d in data:
        if d > 0:
            answer += 1

    if answer > 0:
        answer -= 1
    else:
        answer = 0
    print(answer)
    return answer