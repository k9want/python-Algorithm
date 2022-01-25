# 각 종류별로 가지 수를 알아본다 19가지
# 그 가짓수에 대해 반복으로 가장 큰 것을 찾는다.
# 문제 푸는 로직은 간단하지만 실수 주의


n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        # # 일자
        if j + 3 < m:
            temp = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i][j + 3]
            if ans < temp: ans = temp
        if i + 3 < n:
            temp = a[i][j] + a[i + 1][j] + a[i + 2][j] + a[i + 3][j]
            if ans < temp: ans = temp
        #  네모
        if i + 1 < n and j + 1 < m:
            temp = a[i][j] + a[i][j + 1] + a[i + 1][j] + a[i + 1][j + 1]
            if ans < temp: ans = temp

        # ㄴ자
        if i + 2 < n and j + 1 < m:
            temp = a[i][j] + a[i + 1][j] + a[i + 2][j] + a[i + 2][j + 1]
            if ans < temp:
                ans = temp
        if i + 2 < n and j + 1 < m:
            temp = a[i][j] + a[i + 1][j] + a[i + 2][j] + a[i][j + 1]
            if ans < temp:
                ans = temp
        if i + 2 < n and j + 1 < m:
            temp = a[i][j] + a[i][j + 1] + a[i + 1][j + 1] + a[i + 2][j + 1]
            if ans < temp:
                ans = temp
        if i + 2 < n and j - 1 >= 0 :
            temp = a[i][j] + a[i + 1][j] + a[i + 2][j] + a[i + 2][j - 1]
            if ans < temp:
                ans = temp
        if i + 1 < n and j + 2 < m:
            temp = a[i][j] + a[i + 1][j] + a[i][j + 1] + a[i][j + 2]
            if ans < temp:
                ans = temp
        if i + 1 < n and j + 2 < m:
            temp = a[i][j] + a[i + 1][j + 2] + a[i][j + 1] + a[i][j + 2]
            if ans < temp:
                ans = temp
        if i + 1 < n and j + 2 < m :
            temp = a[i][j] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 1][j + 2]
            if ans < temp:
                ans = temp
        if i - 1 >= 0 and j + 2 < m :
            temp = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i - 1][j + 2]
            if ans < temp:
                ans = temp

        #  ㄹ

        if i + 2 < n and j + 1 < m:
            temp = a[i][j] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 2][j + 1]
            if ans < temp:
                ans = temp
        if i + 2 < n and j - 1 >= 0 :
            temp = a[i][j] + a[i+1][j] + a[i+1][j-1] + a[i+2][j-1]
            if ans < temp: ans = temp
        if i + 1 < n and j + 2 < m :
            temp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+1][j + 2]
            if ans < temp: ans = temp

        if i - 1 >= 0 and j + 2 < m:
            temp = a[i][j] + a[i][j+1] + a[i-1][j + 1] + a[i-1][j + 2]
            if ans < temp: ans = temp

        #  ㅜ

        if i + 1 < n and j + 2 < m :
            temp = a[i][j] + a[i][j+1] + a[i][j + 2] + a[i+1][j+1]
            if ans < temp: ans = temp

        # ㅏ
        if i + 2 < n and j + 1 < m :
            temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+1][j + 1]
            if ans < temp: ans = temp
        # ㅗ
        if i - 1 >= 0 and j + 2 < m :
            temp = a[i][j] + a[i][j+1] + a[i][j + 2] + a[i-1][j+1]
            if ans < temp: ans = temp

        # ㅓ
        if i + 2 < n and j - 1 >= 0:
            temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+1][j-1]
            if ans < temp: ans = temp

print(ans)