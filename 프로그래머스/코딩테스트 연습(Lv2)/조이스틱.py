"""
- 알파벳 바꾸는 횟수는 ord()를 이용해서 정수로 바꾼후 빼기로 a - s, z - s + 1
- 이동은 한쪽으로만 이동하는 것, 왼쪽이동후 오른쪽으로 이동, 오른쪽이동후 왼쪽으로 이동하는 세 개를 최솟값으로

"""


def solution(name):
    answer = 0

    minn = len(name) - 1
    next = 0
    for i, c in enumerate(name):
        # 변경 방향을 위로 할지 아래로 할지
        answer += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)

        # 다음 알파벳 찾기(A)를 찾는다.
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 방향 전환없이 무조건 왼쪽에서 오른쪽으로, 오른쪽으로 갔다가 왼쪽으로 가는 것, 왼쪽으로 갓다가 오른쪽으로 가는 것
        minn = min(minn, i + i + len(name) - next, i + 2 * (len(name) - next))

    answer += minn

    return answer