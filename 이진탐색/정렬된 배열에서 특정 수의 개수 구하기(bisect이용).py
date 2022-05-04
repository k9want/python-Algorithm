"""
아이디어
문제에서 시간복잡도 O(logN)언급
이진탐색으로 구현

입력
7 2
1 1 2 2 2 2 3
출력
4

"""

from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):

    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    return right_index - left_index


n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

result = count_by_range(array, m, m)
print(result if result > 0 else -1)


