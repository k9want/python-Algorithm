def solution(a, b):
    answer = 0

    if a == b:
        return a

    if a > b:
        tmp = b
        b = a
        a = tmp

    for n in range(a, b + 1):
        answer += n

    return answer