"""
1.아이디어
해당 값을 가진 가장 왼쪽의 인덱스를 구하는 이진탐색함수과
가장 오른쪽의 인덱스를 구하는 이진탐색함수를 각각 만들어서 구하고
오른쪽 인덱스 - 왼쪽 인덱스 + 1을 해준다.

2.시간복잡도
이진탐색을 사용 O(logN)



입력
7 2
1 1 2 2 2 2 3
출력
4
------
입력
7 4
1 1 2 2 2 2 3
출력
-1
"""
#해당 값을 가진 가장 왼쪽 인덱스 찾기
def left_index(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # target이고 첫번째거나 아니면 바로 전 인덱스가 target보다 작으면!
    if array[mid] == target and (mid == 0 or array[mid-1] < target):
        return mid
    elif array[mid] > target:
        return left_index(array, target, start, mid-1)
    else:
        return left_index(array, target, mid+1, end)

#해당 값을 가진 가장 오른쪽 인덱스 찾기
def right_index(array, target, start, end):
    if start > end:
        return 'None'
    mid = (start + end) // 2
    if array[mid] == target and (mid == end-1 or array[mid+1] > target):
        return mid
    elif array[mid] > target:
        return right_index(array, target, start, mid-1)
    else:
        return right_index(array, target, mid+1, end)


def count_index(array, target, start, end):
    left = left_index(array, target, start, end)

    if left == None:
        return -1

    else:
        right = right_index(array, target, start, end)
        return right - left + 1



n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

print(count_index(array, m, 0, n-1))






