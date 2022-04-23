"""
1. 아이디어
- 브루트포스, 백트래킹(예전꺼) 재귀함수 안에서, for 돌면서 숫자 선택
- 재귀함수에서 M개를 선택할경우(종료조건 전에) print 
- M으로 갔다가 돌아올때는 원상복구(pop)를 한다.
- 중복가능하고 비내림차순이므로 반복문 안에서 재귀함수 호출할 때 start를 그대로 가져가서 호출하도록 한다.  

2. 시간복잡도
- N^N

3. 자료구조
- 결과값 저장 int []
"""""

import sys
input = sys.stdin.readline

n, m = map(int,input().split())

result = []

def recur(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for i in range(start, n+1):
        result.append(i)
        recur(i)
        result.pop()

recur(1)