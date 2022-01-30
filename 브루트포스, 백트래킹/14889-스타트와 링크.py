"""
1. 아이디어
- 모든 사람을 두 팀으로 나누고 모든 경우의 차이의 최솟값을 구해야한다.
- 각 사람별로 1,2번 팀 중 하나의 팀에 선택되도록 경우의 수를 따진다. 

재귀를 사용할 때 고려할 것 
1. 다음 경우를 호출
    1번 팀 선택할 경우 : recur(index + 1, first + [index], second)
    2번 팀 선택할 경우 : recur(index + 1, first , second + [index])
2. 불가능한 경우
    n/2보다 팀원이 더 많을 때
3. 정답인 경우
    index == n

2. 시간복잡도
2^N
"""""

def recur(index, first, second):
    if index == n:
        if len(first) != n//2:
            return -1
        if len(second) != n//2:
            return -1
        t1 = 0
        t2 = 0
        for i in range(n//2):
            for j in range(n//2):
                if i == j:
                    continue
                t1 += data[first[i]][first[j]]
                t2 += data[second[i]][second[j]]
        diff = abs(t1 - t2)
        return diff
    ans = -1
    t1 = recur(index+1, first+[index], second)
    if ans == -1 or (t1 != -1 and ans > t1):
        ans = t1
    t2 = recur(index+1, first, second+[index])
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    return ans

n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
print(recur(0,[],[]))
