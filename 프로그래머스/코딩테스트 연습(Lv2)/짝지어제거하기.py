"""
스택 특징을 활용

"""
def solution(s):
    answer = -1

    stk = []
    for i in range(len(s)):
        if not stk:
            stk.append(s[i])
        else:
            if stk[-1] == s[i]:
                stk.pop()
            else:
                stk.append(s[i])

    if not stk:
        answer = 1
    else:
        answer = 0

    return answer