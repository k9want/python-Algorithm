def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 'yes'
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 'no'


n = int(input())
array = list(map(int,input().split()))
m = int(input())
check = list(map(int, input().split()))

for c in check:
    print(binary_search(array, c, 0, n-1), end=' ')