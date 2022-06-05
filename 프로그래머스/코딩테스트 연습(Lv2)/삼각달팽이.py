
def solution(n):
    answer = []
    arr = [[0] * n for _ in range(n)]

    y, x = -1, 0
    num = 1
    for j in range(n):
        for i in range(j, n):
            if j % 3 == 0:
                y += 1
            elif j % 3 == 1:
                x += 1
            elif j % 3 == 2:
                y -= 1
                x -= 1
            arr[y][x] = num
            num += 1

    for ar in arr:
        for a in ar:
            if a:
                answer.append(a)



    return answer