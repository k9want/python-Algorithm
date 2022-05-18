"""
완전탐색
처음부터 끝까지 조건에 맞게 탐색하는 코드를 작성

S = 1제곱
D = 2제곱
T = 3제곱
* 해당점수와 바로전에 얻은 점수 2배로 (처음도 가능 처음이면 해당점수만 2배)
# 당첨시 해당 점수 마이너스 * (-1)
숫자가 10일경우가 있기 때문에
숫자를 따로 저장할 변수를 만든다.

"""

def solution(dartResult):
    n = ''
    data = []
    for d in dartResult:
        if d.isdigit():
            n += d
        elif d == 'S':
            n = int(n) ** 1
            data.append(n)
            n = ''
        elif d == 'D':
            n = int(n) ** 2
            data.append(n)
            n = ''

        elif d == 'T':
            n = int(n) ** 3
            data.append(n)
            n = ''

        elif d == '#':
            data[-1] = data[-1] * -1
        elif d == '*':
            if len(data) > 1:
                data[-1], data[-2] = data[-1] * 2, data[-2] * 2
            else:
                data[-1] = data[-1] * 2

    print(data)
    return sum(data)