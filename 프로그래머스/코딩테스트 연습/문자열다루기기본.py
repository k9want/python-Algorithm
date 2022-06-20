def solution(s):
    answer = True

    if len(s) == 4:
        answer = True
    elif len(s) == 6:
        answer = True
    else:
        answer = False

    for i in s:
        if not i.isdigit():
            answer = False
            break

    return answer