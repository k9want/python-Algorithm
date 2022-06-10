#1.상하 반전
#2. reverse()
#3. 오른쪽 90도 회전
#4. 왼쪽 90도
#5,6은 n/2 m/2로 4개로 나누고
#4 1번그룹을 2번으로 2번은 3번으로 3 -> 4 4->1
#6 1 -> 4 4 > 3 3> 2 2> 1
import copy
def func1(arr):
    tmp = 0
    for y in range(n//2):
        for x in range(m):
            tmp = arr[y][x]
            arr[y][x] = arr[n-y-1][x]
            arr[n-y-1][x] = tmp
    return arr


def func2(arr):
    for a in arr:
        a.reverse()
    return arr

#오른쪽90도
def func3(arr):
    m = len(arr[0])
    n = len(arr)
    copy_arr = [[0] * n for _ in range(m)]
    for y in range(m):
        for x in range(n):
            copy_arr[y][x] = arr[n-x-1][y]

    return copy_arr, m, n

#왼쪽 90도
def func4(arr):
    m = len(arr[0])
    n = len(arr)
    copy_arr = [[0] * n for _ in range(m)]
    for y in range(m):
        for x in range(n):
            copy_arr[y][x] = arr[x][m-y-1]

    return copy_arr, m, n

def func5(arr):
    copy_arr = copy.deepcopy(arr)

    #4 -> 1
    for y in range(n//2):
        for x in range(m//2):
            copy_arr[y][x] = arr[y+(n//2)][x]
    # 2-> 3
    for y in range(n//2, n):
        for x in range(m//2, m):
            copy_arr[y][x] = arr[y-(n//2)][x]
    # 1 -> 2
    for y in range(n//2):
        for x in range(m//2, m):
            copy_arr[y][x] = arr[y][x-(m//2)]
    # 3 -> 4
    for y in range(n//2, n):
        for x in range(m//2):
            copy_arr[y][x] = arr[y][x+(m//2)]

    # for a in arr:
    #     print(a)

    return copy_arr


def func6(arr):
    copy_arr = copy.deepcopy(arr)

    #2 -> 1
    for y in range(n//2):
        for x in range(m//2):
            copy_arr[y][x] = arr[y][x+(m//2)]
    # 4-> 3
    for y in range(n//2, n):
        for x in range(m//2, m):
            copy_arr[y][x] = arr[y][x-(m//2)]
    # 3 -> 2
    for y in range(n//2):
        for x in range(m//2, m):
            copy_arr[y][x] = arr[y+(n//2)][x]
    # 1 -> 4
    for y in range(n//2, n):
        for x in range(m//2):
            copy_arr[y][x] = arr[y-(n//2)][x]

    # for a in arr:
    #     print(a)

    return copy_arr



n, m, r = map(int, input().split())
array = []
for y in range(n):
    array.append(list(map(int, input().split())))
data = list(map(int,input().split()))

for d in data:
    if d == 1:
        array = func1(array)
    elif d == 2:
        array = func2(array)
    elif d == 3:
        array, n, m = func3(array)

    elif d == 4:
        array, n, m = func4(array)

    elif d == 5:
        array = func5(array)
    else:
        array = func6(array)

for ar in array:
    print(*ar)


