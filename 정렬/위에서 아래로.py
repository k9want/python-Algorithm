n = int(input())
array = []

for i in range(n):
    array.append(int(input()))

result = sorted(array, reverse=True)
print(*result)
