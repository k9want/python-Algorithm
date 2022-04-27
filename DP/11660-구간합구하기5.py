"""
이중 반복문을 사용시 시간초과가 난다. O(N^2)이기 때문에
그래서 알아보니 누적합 유형이라고 한다.
"""
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

data = []
sum_data = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    data.append(list(map(int,input().split())))

for i in range(1, n+1):
    for j in range(1, n+1):
        sum_data[i][j] = data[i-1][j-1] + sum_data[i-1][j] + sum_data[i][j-1] - sum_data[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int,input().split())

    print(sum_data[x2][y2] - sum_data[x1-1][y2] - sum_data[x2][y1-1] + sum_data[x1-1][y1-1])