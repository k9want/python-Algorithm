"""
아이디어 - 데이터 수가 많다 우선 이진탐색을 고려해보자
주의 이진탐색은 정렬이 된 상태에서 사용가능!!
파라메트릭 서치 유형 문제 - 반복문 구현 용이
거리의 최댓값
"""
import sys
input = sys.stdin.readline
n, c = list(map(int,input().split()))
array = []
for i in range(n):
    array.append(int(input()))
array.sort()

start = 1
end = array[-1] - array[0]
result = 0

while(start <= end):
    mid = (start + end) // 2
    target = array[0]
    count = 1

    for i in range(1, n):
        if array[i] >= target + mid:
            target = array[i]
            count += 1

    if count >= c:
            start = mid+1
            result = mid
    else:
            end = mid-1

print(result)