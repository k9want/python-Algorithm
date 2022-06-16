from collections import deque

def rotate_start(idx, direction):
    left_tmp = data[idx][6]
    left_d = direction

    #왼쪽
    for i in range(idx, 0, -1):
        if left_tmp != data[i-1][2]:
            left_tmp = data[i-1][6]
            data[i-1].rotate(left_d * -1)
            left_d *= -1
        else:
            break
    right_tmp = data[idx][2]
    right_d = direction
    for j in range(idx, n-1):
        if right_tmp != data[j+1][6]:
            right_tmp = data[j+1][2]
            data[j+1].rotate(right_d * -1)
            right_d *= -1
        else:
            break

n = int(input())
data = []
for _ in range(n):
    data.append(deque(map(int, input())))
k = int(input())
for _ in range(k):
    num, direction = map(int, input().split())
    rotate_start(num-1, direction)
    data[num-1].rotate(direction)


cnt = 0
for i in range(n):
    if data[i][0]:
       cnt += 1

# for d in data:
#     print(d)
print(cnt)


