"""
나의 풀이
복잡하게 생각했다...
"""
def solution(s):
    arr = list(s)
    zero = 0
    count = 0
    while True:
        if len(s) == 1 and s == '1':
            break
        arr = list(s)
        arr.sort()
        # 0찾기
        index = arr.index('1')
        zero += (len(arr[:index]))
        s = bin(len(arr[index:]))[2:]

        count += 1

    return [count, zero]

"""
0과 1로만 이루어진 문자열이니까 
len(s) - len(문자열 내 1의 갯수)하면 0의 개수가 나오고 
bin(1의 개수)[2:]가 곧 길이를 2진법으로 바꾼 것으로 생각할 수 있다. 
"""


def solution(s):
    cnt, zero = 0, 0

    while s != '1':
        cnt += 1
        one = s.count('1')
        zero += len(s) - one
        s = bin(one)[2:]

    return [cnt, zero]