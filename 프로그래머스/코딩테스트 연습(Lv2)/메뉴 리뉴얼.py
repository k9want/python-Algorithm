"""
조합으로 선택하고
주의 정렬을 한 뒤에!!!
Counter를 통해 개수를 파악한다.
most_common()을 사용해도 되고 만약 기억나지 않는다면!!
for c in count:
  cnt.append((c, count[c])
이처럼 직접 로직을 구현한 후에 오름차순 정렬하고
제일 많은 횟수를 가진 메뉴조합을 출력하도록 코드를 작성한다.

Counter와 Collections을 사용해서 해결한 문제
"""
from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for c in course:
        result = []
        cnt = []
        for o in orders:
            for co in list(combinations(o, c)):
                rs = ''.join(sorted(co))
                result.append(rs)

        count = Counter(result)
        for c in count:
            cnt.append((c, count[c]))
        cnt.sort(key=lambda x: -x[1])
        # print(cnt)
        if len(cnt) > 1 and cnt[0][1] > 1:
            i = 0
            while True:
                if cnt[i][1] == cnt[0][1]:
                    answer.append(cnt[i][0])
                    i += 1
                else:
                    break

        # for c in count:

    answer.sort()

    return answer