def binary_search(array, target, start, end):
    if start > end:
        return 'no'
    mid = (start + end) // 2
    if array[mid] == target:
        return 'yes'
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid+1, end)




n = int(input())
array = list(map(int,input().split()))
m = int(input())
check = list(map(int, input().split()))

for c in check:
    print(binary_search(array, c, 0, n-1), end=' ')



