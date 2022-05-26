"""
핵심:
 복잡할 경우에는 함수로 나눠서 생각하자
 함수를 만들때 더 효율적으로 작성하는것을 생각하자
 어렵게 생각하지말고 간단하게 count대신 하나하나 직접 세기
 재귀를 사용할 수 있다는 점도 알아둘것
"""

"""
하나하나 복잡한 과정을 함수로 나눠서 생각해보자
"""


# u, v나누기 count를 이용해서 하는 것 if u.count('(') == u.count(')') 보다 직접 세는 게
def divide(p):
    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return p[:i + 1], p[i + 1:]


# u가 올바른 괄호인지 확인하기
def check(u):
    """
    내가 구현했던 코드 stk이 비어있는지 아닌지로 하지만 더 좋은 방법은 중간에 아니면 바로 결과가 나오도록 하는 것
    이미 균형잡힌 괄호라고 생각하고 코드를 짜는 것
    result = False
    stk = []
    for ui in u:
        if not stk:
            stk.append(ui)
        else:
            if stk[-1] == '(' and ui == ')':
                stk.pop()
            else:
                stk.append(ui)
    if not stk:
        result = True
    return result
    """
    stk = []
    for ui in u:
        if ui == '(':
            stk.append(ui)
        else:
            if not stk:
                return False
            stk.pop()

    return True


def solution(p):
    answer = ''

    # 1.
    if not p:
        return ''
    # 2.
    u, v = divide(p)
    # 3.
    if check(u):
        # 3-1
        # 재귀 이용 <- 이건 생각 못했다....
        return u + solution(v)
    # 4.
    else:
        # 4-1
        answer += '('
        # 4-2
        answer += solution(v)
        # 4-3
        answer += ')'
        # 4-4
        for ui in u[1: len(u) - 1]:
            if ui == '(':
                answer += ')'
            else:
                answer += '('

        return answer