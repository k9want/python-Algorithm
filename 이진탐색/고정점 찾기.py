"""
5
-15 -6 1 3 7
3

7
-15 -4 2 8 9 13 15
2

7
-15 -4 3 8 9 13 15
-1
"""
def fixed_point(array, start, end):
    if start > end:
        return -1
    mid = (start+end)//2
    if array[mid] == array.index(array[mid]):
        return mid
    elif array[mid] > array.index(array[mid]):
        return fixed_point(array, start, mid-1)
    else:
        return fixed_point(array, mid+1, end)


n = int(input())
array = list(map(int, input().split()))

print(fixed_point(array, 0, n-1))
