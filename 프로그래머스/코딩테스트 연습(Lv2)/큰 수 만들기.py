"""
시간복잡도 고려 완전탐색이나 순열로 뽑아서 사용하는 것은 안됨
스택을 이용해서 풀었다.
마지막 주의할 점은 남은 숫자가 같은데 k가 아직 0이 아니라면 k만큼 길이를 빼준다.
https://programmers.co.kr/learn/courses/30/lessons/42883#
"""


def solution(number, k):
    answer = []

    for n in number:
        while answer and k > 0 and answer[-1] < n:
            answer.pop()
            k -= 1

        answer.append(n)

    answer = ''.join(answer[:len(answer) - k])
    return answer