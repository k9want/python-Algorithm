"""
그리디 문제
오름차순으로 정렬하고
조회할 때마다 cnt에 1을 추가해서 cnt가 같거나 클경우에 result에 +1을 하는 방식
"""

n = int(input())
data = list(map(int, input().split()))

data.sort()

cnt = 0
result = 0
for d in data:
    cnt += 1
    if d <= cnt:
        result += 1
        cnt = 0

print(result)



"""
5
2 3 1 2 2
"""
