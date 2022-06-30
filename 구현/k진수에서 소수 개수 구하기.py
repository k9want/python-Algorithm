"""
우선 진수를 바꾸는 함수와
소수를 판별하는 함수를 하나씩 구현한뒤
조건에서는 0을 기준으로 각각의 조건 네가지가 있기 때문에
진수로 바꾼 결과를 0으로 각각 나눠서 판단한다. 1은 어짜피 소수가 아니므로 이 같은 방법을 사용할 수 있다.
또한 P가 0이 포함하면 안되기때문에 가능 !!!
"""


def convert(n, k):
    result = ''
    while n > 0:
        result += str(n % k)
        n = n // k
    return result[::-1]


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0

    # 일단 k 진수로 교체
    cvt = convert(n, k)

    # 소수인지 판별
    for cv in cvt.split('0'):
        if cv.isdigit() and is_prime(int(cv)):
            answer += 1

    return answer