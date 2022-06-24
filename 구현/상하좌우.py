n = int(input())

x = 1
y = 1

data = input().split()
# print(data)
dy = [0,0,-1,1]
dx = [-1,1,0,0]
moves = ['L','R','U','D']


for d in data:
    for i in range(4):
        if moves[i] == d:
            ny = y + dy[i]
            nx = x + dx[i]

    if 0 < ny <= n and 0 < nx <= n:
        x = nx
        y = ny

print(y, x)





# for d in data:
#     for i in range(4):
#         if moves[i] == d:
#             ny = dy[i] + y
#             nx = dx[i] + x
#
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     x = nx
#     y = ny
#
# print(x, y)

"""
5
R R R U D D
"""