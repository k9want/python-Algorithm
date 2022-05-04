"""
5
8 3 7 9 2
3
5 7 9
"""
n = int(input())
#계수정렬을 위해 공간 만들기
array = [0] * 1000001

for i in input().split():
    array[int(i)] += 1

m = int(input())
check = list(map(int, input().split()))

for c in check:
    if array[c] >= 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
