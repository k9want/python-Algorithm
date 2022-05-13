"""
문제를 보면 바로 스택유형이라는 것이 떠올려진다.
뽑아서 stk에 넣고
스택의 길이가 2이상일때 스택의 두 원소가 같다면 answer += 2를 하고
스택의 해당 두 원소를 제거한다.
pop()으로 제거했음
"""
def solution(board, moves):
    answer = 0
    stk = []

    for m in moves:
        for b in board:
            if b[m - 1] != 0:
                stk.append(b[m - 1])
                b[m - 1] = 0
                break

        if len(stk) >= 2 and stk[-1] == stk[-2]:
            answer += 2
            stk.pop()
            stk.pop()

    return answer