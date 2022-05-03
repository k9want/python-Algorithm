"""
내림차순 -
오름차순 +
key에 람다함수로 정렬기준 설정하는 문제
"""

import sys
input = sys.stdin.readline
n = int(input())
array = []

for _ in range(n):
    array.append(input().split())

array.sort(key=lambda arr: (-int(arr[1]), int(arr[2]), -int(arr[3]), arr[0]))

for arr in array:
    print(arr[0])