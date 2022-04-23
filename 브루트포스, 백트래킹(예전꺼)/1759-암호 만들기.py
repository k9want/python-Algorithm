"""
1. 아이디어
- 오름차순을 위해 우선 암호를 만들기 전에 정렬부터!
- 길이에 맞게 재귀를 이용해서 암호를 전부 만들고 
- 그 후에 각각 모음과 자음이 해당 조건에 맞는지 검사를 해서 출력하는 방법으로 구현

2. 시간복잡도
2^C * L
"""""
# 선택으로 풀기
def check(password):
    mo = 0
    ja = 0
    for p in password:
        if p in 'aeiou':
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1

def recur(n, al, password, i):
    if len(password) == n:
        if check(password):
            print(password)
        return
    # 불가능한 조건
    if i == len(al):
        return
    # 알파벳이 선택되거나
    recur(n, al, password+a[i], i+1)
    # 선택되지 않거나
    recur(n, al, password, i+1)

n, m = map(int,input().split())
a = input().split()
a.sort()


# recur(n, a, "", 0)


# 순서로 풀기
def check(password):
    mo = 0
    ja = 0
    for p in password:
        if p in 'aeiou':
            mo += 1
        else:
            ja += 1
    if ja >= 2 and mo >= 1:
        print(''.join(map(str, password)))
    return

def recur(start):
    if len(result) == n:
        check(result)
        return
    if len(result) > n:
        return
    for i in range(start, m):
        if a[i] not in result:
            result.append(a[i])
            # print(a[i])
            recur(i+1)
            result.pop()



n, m = map(int,input().split())
a = list(input().split())
a.sort()
result = []
recur(0)
