# 검사
def check(data):
    n = len(data)
    ans = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if data[i][j] == data[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
        cnt = 1
        for j in range(1, n):
            if data[j][i] == data[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
    return ans


n = int(input())
data = [list(input()) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        # 아래에 교환 다만 맨 아래는 불가능하니까 조건제시하고
        if i + 1 < n:
            data[i][j], data[i + 1][j] = data[i + 1][j], data[i][j]
            temp = check(data)
            if ans < temp:
                ans = temp
            data[i + 1][j], data[i][j] = data[i][j], data[i + 1][j]
        if j + 1 < n:
            data[i][j], data[i][j + 1] = data[i][j + 1], data[i][j]
            temp = check(data)
            if ans < temp:
                ans = temp
            data[i][j+1], data[i][j] = data[i][j], data[i][j + 1]

print(ans)

# for i in range(3):
#     for j in range(3):
#         print(i, j)


# for i in range(3):
#     for j in range(1, 3):
#         print(i, j - 1)
#
# print('--------------------')
# for i in range(3):
#     for j in range(2):
#         print(i, j + 1)
