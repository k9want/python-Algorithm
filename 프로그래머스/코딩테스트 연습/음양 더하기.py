"""
이것도 바로 가능
부호에 따라 더할지 뺄지를 정하면 된다.
"""


def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer