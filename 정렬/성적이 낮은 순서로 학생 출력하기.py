import sys
input = sys.stdin.readline

n = int(input())

array = []
for i in range(n):
    name, grade = input().split()
    array.append((name, grade))
# 함수 구현으로
# def setting(data):
#     return data[1]
# result = sorted(array, key=setting)

#람다
result = sorted(array, key=lambda arr: arr[1])

for r in result:
    print(r[0], end=' ')
