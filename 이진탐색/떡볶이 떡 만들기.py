n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0

while(start <= end):
    total = 0
    mid = (start + end) // 2
    for arr in array:
        if arr > mid:
            total += arr - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)