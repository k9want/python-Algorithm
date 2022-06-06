"""
dp와 bfs가 섞여있는듯한 문제
if를 각각 사용해서
m : monitor 화면의 이모티콘 개수
c : clipboard에 있는 이모티콘개수
data[m][c]를 이용해서 data[m][?] 이때 가장 작은 수를 찾아서 출력해준다.
"""
from collections import deque
s = int(input())
data = [[0] * (s+1) for _ in range(s+1)]
q = deque()
#화면 개수, 클립보드 개수 data[1][0]
q.append((1,0))
while q:
    m, c = q.popleft()
    #첫번째 클립보드에 복사
    if not data[m][m]:
        data[m][m] = data[m][c] + 1
        q.append((m,m))
    #화면에 붙여넣기
    if m+c <= s and not data[m+c][c]:
        data[m+c][c] = data[m][c]+ 1
        q.append((m+c, c))
    #화면에서 하나 빼기
    if m-1 >= 0 and not data[m-1][c]:
        data[m-1][c] = data[m][c] + 1
        q.append((m-1, c))
result = 999999999
for i in range(s+1):
    if data[s][i]:
        if result > data[s][i]:
            result = data[s][i]

print(result)



