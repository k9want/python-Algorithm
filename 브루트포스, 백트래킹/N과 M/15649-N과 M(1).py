"""
1. 아이디어
- 브루트포스, 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택(방문여부 확인)
- 재귀함수에서 M개를 선택할경우(종료조건 전에) print 
- M으로 갔다가 돌아올때는 원상복구를 한다. 

2. 시간복잡도
- N!

3. 자료구조
- 결과값 저장 int []
- 방문여부 체크 bool []
"""""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []
visited = [False] * (n + 1)


# 흔한 브루트포스, 백트래킹 패턴 암기할 것
def recur(num):
    if num == m:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n + 1):
        if visited[i] == False:
            visited[i] = True
            result.append(i)
            recur(num + 1)
            # 갔다가 돌아올 때 원상복구용 코드
            visited[i] = False
            result.pop()

recur(0)
