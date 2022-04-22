from collections import deque

n, m = map(int, input().split())
deque = deque(range(1, n+1))

print('<', end='')
while True:
    if not deque:
        break
    if len(deque) == 1:
        print(deque.popleft(), end='')
    else :
        deque.rotate(-(m-1))
        print(deque.popleft(), end=', ')

print('>')



