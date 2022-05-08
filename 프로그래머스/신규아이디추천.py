#https://programmers.co.kr/learn/courses/30/lessons/72410/solution_groups?language=python3&type=my

#나의 풀이
from collections import deque

def solution(new_id):


    #1단계
    new_id = new_id.lower()

    second = []
    #2단계
    for i in new_id:
        if i.islower() or i.isdecimal() or i == '-' or i == '_' or i =='.':
            second.append(i)
    three = []
    #3단계
    chk = 0
    for i in range(len(second)):
        if second[i] == '.':
            chk += 1
        else:
            if chk != 0:
                three.append('.')
                chk = 0
            three.append(second[i])
    four = deque(three)
    #4단계
    while four:
        if four[0] != '.' and four[-1] != '.':
            break
        if four[0] == '.':
            four.popleft()
        if four[-1] == '.':
            four.pop()


    four = list(four)

    #5단계
    if not four:
        four.append('a')

    #6단계
    if len(four) >= 16:
        four = four[0:15]
        while four[-1] == '.':
            four.pop()


    #7단계
    while len(four) <= 2:
        four.append(four[-1])

    print(four)
    answer = ''.join(four)
    return answer

#좋은 풀이(1) 3번째 과정에서 replace로 대체했다는 점
def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer

#좋은 풀이(2) - 정규식 이용
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st