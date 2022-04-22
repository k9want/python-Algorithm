# cursor를 기준으로 left, right로 나눈다.
# 둘 다 스택으로 풀었음.
# 여전히 주의할 점 stk.pop()할 때는 stk이 비어있지 않은지 항상 고려할 것

import sys

left = list(input())
right = []

for _ in range(int(input())):
    input = sys.stdin.readline().rstrip
    cmd = input().split()
    if cmd[0] == 'P':
        left.append(cmd[1])
    if cmd[0] == 'L':
        if left:
            data = left.pop()
            right.append(data)
    if cmd[0] == 'D':
        if right:
            data = right.pop()
            left.append(data)

    if cmd[0] == 'B':
        if left:
            left.pop()


if right:
    left.extend(right[::-1])

for l in left:
    print(l, end='')

