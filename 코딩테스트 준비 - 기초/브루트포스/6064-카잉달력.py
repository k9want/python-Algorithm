# 제한 수가 40000  mn= 16억가지
num = int(input())

for _ in range(num):
    # 입력받고
    m, n, x, y = map(int,input().split())
    x -= 1
    y -= 1
    k = x
    while k < n*m:
        if k % n == y:
            print(k+1)
            break
        k += m
    else:
        print(-1)