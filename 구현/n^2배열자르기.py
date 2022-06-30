"""
당연히 n의 최대치가 10^7이기 때문에 이중반복문을 사용하면 안된다.
그래서 고민해보니
각각 좌표라고 생각했을 때 큰 좌표가 큰 값이 됐다는 것을 이용
후에는 간단히 구현으로 풀 수 있었다.
문제를 풀때 좀더 새로운 아이디어가 필요한듯 싶었다.
"""


def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        a = i // n
        b = i % n
        result = max(a, b)
        answer.append(result + 1)

    return answer