"""
stk을 이용
"""


def solution(s):
    answer = True

    stk = []

    for c in s:
        # print(stk)
        if c == ')':
            if not stk:
                return False
            else:
                if stk[-1] == '(':
                    stk.pop()
                elif stk[-1] == ')':
                    stk.append(c)

        else:
            stk.append(c)

    if stk:
        return False

    return True