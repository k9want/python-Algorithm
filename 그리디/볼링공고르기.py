"""
볼링공 범위가 1부터 10까지인 것을 이용
볼링공 무게마다 +1을 해서 볼링공들의 무게별 개수 정보를 가진 리스트를 만들고
리스트를 조회하면서 경우의 수들을 더해나간다.
"""
n, m = map(int,input().split())
data = list(map(int, input().split()))

data.sort()

weights = [0] * 11

for d in data:
    weights[d] += 1

result = 0

for i in range(1, m+1):
    n -= weights[i]
    result += weights[i] * n

print(result)
"""
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2
"""