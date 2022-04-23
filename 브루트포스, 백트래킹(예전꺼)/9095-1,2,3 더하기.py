"""""
1. 아이디어
- 3가지의 경우를 생각해서 재귀를 사용한다. (1의 경우, 2의 경우, 3의 경우)
- 각 경우를 거칠 때마다 수를 더하고 해당 n값과 같은지 다른지 비교
- 가능한 경우 불가능한 경우를 판별하는 조건 명시할 것 

2. 시간복잡도 
방법의 개수 최대 각 자리별로 1,2,3 n개 
3^n

3. 자료구조 
- 최종 경우의 수를 print하기 위한 result 변수 
- 재귀함수 사용
"""""

def recur(num, total):
    if num < total:
        return 0
    if num == total:
        return 1
    result = 0
    for i in range(1, 4):
        total += 1
        result += recur(num, total)
    return result

t = int(input())
for _ in range(t):
    n = int(input())
    print(recur(n, 0))
