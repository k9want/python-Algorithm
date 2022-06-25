"""
combinations으로 각각의 치킨집 조합을 구하고
전부 탐색 (완전탐색)
탐색하면서 각각의 조합의 도시의 치킨거리를 구하고
최솟값을 갱신한다.
"""
from itertools import combinations
r, c = map(int, input().split())
chicken, house = [], []

for row in range(r):
    data = list(map(int, input().split()))
    for col in range(r):
        if data[col] == 1:
            house.append((row, col))
        elif data[col] == 2:
            chicken.append((row, col))



#치킨집 중에 m개의 치킨집을 뽑는 조합 계산
comb = list(combinations(chicken, c))

#치킨 거리의 합을 계산
def get_chicken_value(comb):
    result = 0
    for hx, hy in house:
        tmp = 1e9
        for cx, cy in comb:
            tmp = min(tmp, abs(hx-cx) + abs(hy - cy))

        result += tmp
    return result

result = 1e9
for com in comb:
    result = min(result, get_chicken_value(com))

print(result)


