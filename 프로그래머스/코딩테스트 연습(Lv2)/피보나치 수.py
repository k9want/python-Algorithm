"""
[0] = 0
[1] = 1
[2부터는] = [i-1] + [i-2]
"""
def solution(n):
    answer = []
    answer.append(0)
    answer.append(1)

    for i in range(2, n + 1):
        answer.append((answer[i - 1] + answer[i - 2]) % 1234567)

    return answer[-1]