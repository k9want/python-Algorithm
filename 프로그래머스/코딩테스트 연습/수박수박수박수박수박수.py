def solution(n):
    data = ['수','박']
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += data[0]
        elif i % 2 == 1:
            answer += data[1]
    return answer