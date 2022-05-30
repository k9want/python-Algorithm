"""
문자열을 분리해서 대문자 처리후 다시 합친다.!!

"""


def solution(s):
    answer = []
    data = s.split(' ')
    for d in data:
        d = d[:1].upper() + d[1:].lower()
        answer.append(d)

    answer = ' '.join(answer)

    return answer