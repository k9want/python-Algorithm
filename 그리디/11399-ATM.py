# 작은수로 정렬하고
# 더한다.

n = int(input())

pp = list(map(int, input().split()))

pp.sort()

# print(pp)

result = 0
for i in range(n):
    result += sum(pp)
    pp.pop()
    # print(pp)
print(result)