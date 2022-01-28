"""
1. 아이디어
- 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택
- 재귀함수에서 M개를 선택할경우(종료조건 전에) print 
- M으로 갔다가 돌아올때는 원상복구(pop)를 한다.
- 시작점이 바뀌기 때문에 시작점을 넣어줘야 한다.
- 시작점이 다르기 때문에 굳이 방문체크 배열을 사용할 필요는 없다 

2. 시간복잡도
- N^M

3. 자료구조
- 결과값 저장 int []
"""""

# 순서로 푸는 방법
import sys
sys.stdin.readline

n,m = map(int,input().split())
result = []

def recur(start):
    if len(result) == m:
        print(' '.join(map(str,result)))
        return

    for i in range(start, n+1):
        if i not in result:
            result.append(i)
            recur(i + 1)
            result.pop()

recur(1)

# 선택으로 푸는 방법
"""
1. 아이디어
- 함수는 수를 선택할지 안할지를 결정
- 선택된 수의 개수를 체크
- 주의할 점 : 선택이 되든 안되든 체크한 수는 다음 인자로 넘겨야한다.

2. 시간복잡도
- 2^N

3. 자료구조
- 결과값 저장 int []
"""""

n,m = map(int,input().split())
result = [0] * m

def recur(index, selected, n, m):
    if selected == m:
        print(' '.join(map(str, result)))
        return
    if index > n:
        return
    result[selected] = index
    recur(index+1 , selected+1, n, m)
    result[selected] = 0
    recur(index+1,selected,n,m)

recur(1, 0, n, m)