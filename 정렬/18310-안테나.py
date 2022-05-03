"""
단순히 정렬하고 중간값을 찾는 문제
"""

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

array.sort()
print(array[(n-1)//2])