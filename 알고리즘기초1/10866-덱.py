import sys
from collections import deque
dq = deque()

def push_front(x):
    dq.appendleft(x)

def push_back(x):
    dq.append(x)

def pop_front():
    if not dq:
        return -1
    return dq.popleft()

def pop_back():
    if not dq:
        return -1
    return dq.pop()

def size():
    return len(dq)

def empty():
    if not dq:
        return 1
    return 0

def front():
    if not dq:
        return -1
    return dq[0]

def back():
    if not dq:
        return -1
    return dq[-1]


for _ in range(int(input())):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push_front':
        push_front(cmd[1])
    if cmd[0] == 'push_back':
        push_back(cmd[1])
    if cmd[0] == 'pop_front':
        print(pop_front())
    if cmd[0] == 'pop_back':
        print(pop_back())
    if cmd[0] == 'size':
        print(size())
    if cmd[0] == 'empty':
        print(empty())
    if cmd[0] == 'front':
        print(front())
    if cmd[0] == 'back':
        print(back())

