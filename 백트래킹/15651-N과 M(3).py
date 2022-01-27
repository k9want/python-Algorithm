"""
1. 아이디어
- 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택
- 재귀함수에서 M개를 선택할경우(종료조건 전에) print 
- M으로 갔다가 돌아올때는 원상복구(pop)를 한다.
- 전 문제처럼 방문체크는 하지 않아도 된다. 중복가능하기 때문에 

2. 시간복잡도
- N^M

3. 자료구조
- 결과값 저장 int []
"""""
import sys

sys.stdin.readline

n, m = map(int, input().split())
result = []


def recur(num):
    if num == m:
        print(' '.join(map(str, result)))
        return

    for i in range(1, n+1):
        result.append(i)
        recur(num + 1)
        result.pop()


recur(0)
