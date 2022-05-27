"""
역시나 했는데 효율성에서 실패했다.
실패한 코드 시간 초과
info 는 최대 50000
query 최대 100000
50억이 되기때문에 실패
"""

# 조건을 충족하는지
def check(q, i):
    for j in range(len(q) - 1):
        # print(q[j], i[j])
        if q[j] == '-':
            continue
        else:
            if q[j] != i[j]:
                return False
            else:
                continue
    return True
    # print(q[-1], i[-1])


def solution(info, query):
    answer = []

    for q in query:
        result = 0
        data = q.split(' and ')
        f, s = data.pop().split(' ')
        data.append(f)
        data.append(s)
        # print(data)
        for i in info:
            # lang, part, career, food, score
            info_data = i.split(' ')
            # print(info_data)
            if check(data, info_data):
                if int(data[-1]) <= int(info_data[-1]):
                    result += 1
        # print(result)
        answer.append(result)

    return answer


"""
그러면 어떻게 할까?
점수를 제외한 모든 문자열을 키로 설정하고 점수는 값으로 설정한다. 
중요한 것은 각 값을 리스트 형태로 저장하는 것!! 
1. from collections import defaultdict을 이용
   defaultdict(list) 
2. 이를 통해 키 값으로 해당 조건에 맞는 값 리스트를 뽑아서 
이진탐색을 통해서 해당 값 이상인것을 찾는다. bisect_left는 lower bound라고 하는데 특정 값 이상의 인덱스를 찾아준다. 
bisect_right는 upper bound에 대응한다. 
"""
from bisect import bisect_left, bisect_right
from itertools import combinations
from collections import defaultdict


def solution(info, query):
    answer = []

    # info 파싱해서 셋팅하기
    data = defaultdict(list)
    for i in info:
        i = i.split()
        i_key = i[:-1]
        i_value = int(i[-1])

        for j in range(0, 5):
            combi = list(combinations(i_key, j))

            for c in combi:
                # 조합들을 하나의 문자열로 합해서
                tmp = ''.join(c)
                # - print(tmp)
                # 그것을 이용해서 키 : 값을 만든다.
                data[tmp].append(i_value)
                # - print(data)

        # print(data)

    # 이진탐색을 위해 정렬하기 리스트형태인 값을 정렬하는 것!!!
    for key in data.keys():
        data[key].sort()

    # query 셋팅하기
    for q in query:
        q = q.split(' and ')

        food, score = q[-1].split(' ')
        q_key = q[:-1]
        q_key.append(food)
        q_value = score
        while '-' in q_key:
            q_key.remove('-')
        q_key = ''.join(q_key)

        if q_key in data:
            score_list = data[q_key]
            if len(score_list) > 0:
                answer.append(len(score_list) - (bisect_left(score_list, int(q_value))))

        else:
            answer.append(0)

    return answer