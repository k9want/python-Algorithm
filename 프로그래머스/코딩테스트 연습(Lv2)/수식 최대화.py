"""
itertools permutations을 통해 순열로 연산자 우선순위를 뽑고 전부 탐색
+ - * 각각의 연산자를 계산하는 함수(operate)와 그 함수를 이용해서 우선순위별로 계산하는 함수(calcu)를 작성
순열로 나온 모든 경우의 수를 전부 탐색해서 절댓값이 가장 높은 수를 출력
이번에도 하나하나 함수로 만들어가면서 복잡한 것을 간단하게 쪼개서 구현했다.
"""

from itertools import permutations

def operate(n1, n2, op):
    if op == '*':
        return n1 * n2
    elif op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2


def calcu(expression, op):
    # 리스트로 만들고
    num = ''
    data = []
    for e in expression:
        if e == '*' or e == '+' or e == '-':
            data.append(int(num))
            data.append(e)
            num = ''
        else:
            num += e
    data.append(int(num))
    # print(data)

    for o in op:
        stk = []
        while len(data) != 0:
            x = data.pop(0)
            if stk and x == o:
                stk.append(operate(stk.pop(), data.pop(0), x))
            else:
                stk.append(x)
            # print('=====')
            # print(data)
            # print(stk)
        data = stk

    if data[0] < 0:
        return -data[0]

    else:
        return data[0]


def solution(expression):
    answer = 0
    result = []

    op = ['*', '+', '-']
    pe = list(permutations(op, 3))

    for p in pe:
        result.append(calcu(expression, p))

    answer = (max(result))

    return answer