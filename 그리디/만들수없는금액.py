"""
target = 1부터 범위가 정해져있으니까
점차 data안에 원소들을 하나씩 더하면서 target보다 원소가 클 경우 break

"""
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for d in data:
    if target < d:
        break
    target == d
print(target)