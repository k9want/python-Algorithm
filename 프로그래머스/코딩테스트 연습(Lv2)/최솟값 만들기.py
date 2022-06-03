"""
하나는 내림차순 정렬 나머지하나는 오름차순 정렬후 순차적으로 곱해서 더해준다.
"""


def solution(A, B):
    answer = 0

    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer