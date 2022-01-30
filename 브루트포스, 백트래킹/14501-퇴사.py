"""""
1. 다음 경우 호출 생각
기준 : 날짜, 수입 => 재귀함수의 인자로 
 상담을 한다. 
    날짜 + 상담의 날짜기간 + 수입 + 상담수입
 상담을 안한다. 
    날짜 + 1 , 수입 그대로
    
    
2 . 불가능한 경우 : 날짜 > N + 1

시간복잡도
2^N
"""""
n = int(input())
t = [0] * (n+1)
p = [0] * (n+1)

for i in range(1, n+1):
   t[i], p[i] = map(int,input().split())


ans = 0
def recur(day, price):
    global ans
    if day == n+1:
        ans = max(ans, price)
        return
    if day > n+1:
        return
    recur(day+1, price)
    recur(day+t[day], price+p[day])


recur(1, 0)
print(ans)