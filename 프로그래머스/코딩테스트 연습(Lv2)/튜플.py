"""
효율 X -> 어떻게든 풀기 급급했다...
...
"""
def solution(s):
    answer = []
    result = []
    nums = []
    data = list(map(str, s[2:-2].split('},{')))

    # print(data)
    for d in data:
        if len(d) > 1:
            for i in d.split(','):
                answer.append(i)
        else:
            answer.append(d)
    # print(answer)
    set_answer = set(answer)
    for s in set_answer:
        i = answer.count(s)
        result.append((-i, s))
    # print(result)
    for res in sorted(result):
        nums.append(int(res[1]))

    # print(nums)
    return nums

"""
핵심 아이디어 
정렬할 때 sort(key = len) 길이별로 정렬!!!
"""


def solution(s):
    answer = []

    data = list(map(str, s[2:-2].split('},{')))
    new_data = []
    for d in data:
        new_data.append(d.split(','))

    new_data.sort(key=len)
    # print(new_data)

    for n in new_data:
        for i in range(len(n)):
            if int(n[i]) not in answer:
                # print(n[i])
                answer.append(int(n[i]))

    return answer