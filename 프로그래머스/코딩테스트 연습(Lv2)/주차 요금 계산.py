"""
전에 썼던 defaultdict을 바로 사용해봤다.
입출차 기록이 홀수면 값 리스트에 23:59를 추가하고
하나씩 뒤에서부터 pop()하면서 문제를 해결했다.
import math
올림함수 math.ceil()
"""

from collections import defaultdict
import math


def solution(fees, records):
    answer = []

    # records.sort(key = lambda x: (x[1], x[0]))
    data = defaultdict(list)

    for r in records:
        r = r.split(' ')
        data[r[1]].append(r[0])

    for k in data.keys():
        result = 0
        if len(data[k]) % 2 == 1:
            data[k].append('23:59')
        while len(data[k]) != 0:
            outn = data[k].pop()
            inn = data[k].pop()
            oh, om = map(int, outn.split(':'))
            ih, im = map(int, inn.split(':'))
            result += int(((oh - ih) * 60) + (om - im))

        answer.append((k, result))
    answer.sort()

    money = []
    for a in answer:
        if 0 <= a[1] <= fees[0]:
            money.append(fees[1])
        else:
            m = fees[1] + (math.ceil((a[1] - fees[0]) / fees[2]) * fees[3])
            money.append(m)

    return money