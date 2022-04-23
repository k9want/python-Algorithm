"""
아이디어
- 점화식 : An = An-1 + An-2
-이전값, 이전이전값 더해서 10007로 나눠서 저장
-*중요 3부터 N까지 값 구하기

시간복잡도
- O(N)
"""

import sys
input = sys.stdin.readline

n = int(input())
result = [0, 1, 2] #초기값 설정

for i in range(3, n+1):
    result.append((result[i-1] + result[i-2]) % 10007)

print(result[n])



