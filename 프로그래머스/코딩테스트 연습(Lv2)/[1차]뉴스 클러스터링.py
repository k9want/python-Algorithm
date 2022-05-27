"""
괄호변환문제처럼 함수를 만들어서 단순하게 문제를 풀었다.
대소구분이 없기때문에 lower()사용
영어만 가능하기때문에 isalpha()사용
Counter를 이용 min과 max를 사용해서 코드를 작성했다.
"""

from collections import Counter


def makestr(strr):
    data = []
    # len(strr)-1 중요!! 마지막은 하나밖에 없으니까 못만드니까
    for i in range(len(strr) - 1):
        # 영소만 있는지 체크 필요없는 글자 제거
        if strr[i].isalpha() and strr[i + 1].isalpha():
            data.append(strr[i:i + 2])

    return data


def check(strr):
    result = ""
    for s in strr:
        if s.isalpha():
            print(s)
            result += s

    return result


def solution(str1, str2):
    answer = 0
    # 대소구분 x
    str1, str2 = str1.lower(), str2.lower()

    # 두쌍씩 만들기
    s1 = makestr(str1)
    s2 = makestr(str2)
    # print(s1, s2)

    # 자카드 유사도 결국 숫자로 계산하니까
    c1, c2 = Counter(s1), Counter(s2)
    c1 = dict(c1)
    c2 = dict(c2)
    # print(c1)
    minn = 0
    maxn = 0
    for k1 in c1.keys():
        if k1 in c2.keys():
            minn += min(c1[k1], c2[k1])
            maxn += max(c1[k1], c2[k1])
        else:
            maxn += c1[k1]
    for k2 in c2.keys():
        if k2 not in c1.keys():
            maxn += c2[k2]

    if minn == 0 and maxn == 0:
        return 65536
    # print(minn, maxn)
    answer = int(minn / maxn * 65536)

    return answer