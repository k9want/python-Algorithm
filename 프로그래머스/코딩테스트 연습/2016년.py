"""
윤년 2월이 29일까지 있는 해

주의 1월 1일이면 a = 0 이라는 점!!! a-1 !!

"""
def solution(a, b):
    m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    cal = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', ]

    days = 0
    for i in range(a - 1):
        days += m[i]
    days += b
    print(days % 7)

    answer = cal[days % 7]
    return answer