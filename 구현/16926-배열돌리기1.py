import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

#돌리기
def rotate(y, x):
    if y == min(n , m) // 2:
        return
    tmp = data[y][x]
    #위부터
    for i in range(x, m-x-1):
        data[y][i] = data[y][i+1]
    #오른쪽
    for i in range(y, n-y-1):
        data[i][m-x-1] = data[i+1][m-x-1]
    #아래쪽
    for i in range(m-x-1, x, -1):
        data[n-y-1][i] = data[n-y-1][i-1]
    #왼쪽
    for i in range(n-y-1, y, -1):
        data[i][x] = data[i-1][x]
    data[y+1][x] = tmp
    return rotate(y+1, x+1)


while r:
    r -= 1
    rotate(0,0)


for d in data:
    print(*d)
