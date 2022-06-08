"""
p의 값들을 최솟값으로 갱신하면서 푼다.
"""
n = int(input())
p =[0]
p.extend(list(map(int, input().split())))

for i in range(1, n+1):
    for k in range(1, i):
        p[i] = min(p[i], p[i-k] + p[k])
print(p[n])