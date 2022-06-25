"""
기둥과 보가 설치가능한지 체크하는 함수
그리고 시뮬 돌리면서 매번 계속 확인하기
"""
def possible(answer):
    for x, y, a in answer:
        if a == 0:
            # 바닥이거나 보의 왼쪽이거나 보의 오른쪽이거나 바로 밑에 기둥이 있거나
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
                # 만약에 아니면??? 설치불가능
            else:
                return False

        elif a == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []

    for x, y, a, b in build_frame:
        # 삭제
        if b == 0:
            answer.remove([x, y, a])
            if not possible(answer):
                answer.append([x, y, a])
        if b == 1:
            answer.append([x, y, a])
            if not possible(answer):
                answer.remove([x, y, a])

    return sorted(answer)