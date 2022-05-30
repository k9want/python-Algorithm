"""
점프 + 1
순간이동 현재 index * 2
거꾸로 2로 나누고 홀수이면 ans 1을 더해준다. 1일때까지 반복
"""


def solution(n):
    ans = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        elif n % 2 == 1:
            n = n // 2
            ans += 1

    return ans