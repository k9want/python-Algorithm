"""
약수는 나누어서 떨어지는 수
1부터 해당 수까지 계속 나눠서 0이되는 수를 cnt += 1 증가하고
짝수면 더하고
홀수면 빼는 코드 작성
"""

def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer