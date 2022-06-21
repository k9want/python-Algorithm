def solution(seoul):
    result = 0
    for i, v in enumerate(seoul):
        if v == 'Kim':
            result = i
            break

    answer = '김서방은 ' + str(result) + '에 있다'
    return answer