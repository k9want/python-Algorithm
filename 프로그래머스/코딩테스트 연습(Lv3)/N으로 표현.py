"""
규칙 찾기
1. 단순히 이어붙인 수
2. 사칙연산 <- 여기서 규칙 찾기
3. DP인지 아닌지 구분 - 전 결과를 이용했다. 
참고 : https://gurumee92.tistory.com/164
"""

def solution(N, number):
    if N == number:
        return 1

    answer = 0

    # set초기화 8개인이유 최솟값이 8보다 크면 -1return을 하라고 문제에 나왔기 때문
    s = [set() for _ in range(8)]

    # 각 set마다 기본수 "N" * i수로 초기화
    for i, v in enumerate(s, start=1):
        v.add(int(str(N) * i))

    for j in range(1, 8):
        for i in range(j):
            for op1 in s[i]:
                for op2 in s[j - i - 1]:
                    s[j].add(op1 + op2)
                    s[j].add(op1 - op2)
                    s[j].add(op1 * op2)
                    if op2 != 0:
                        s[j].add(op1 // op2)
        if number in s[j]:
            answer = j + 1
            break
        else:
            answer = -1

    return answer