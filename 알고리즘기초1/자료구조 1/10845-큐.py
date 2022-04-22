import sys
from collections import deque

deque = deque()

def push(x):
    deque.append(x)

def pop():
    if not deque:
        return -1
    return deque.popleft()

def size():
    return len(deque)

def empty():
    return 0 if deque else 1

def front():
    if not deque:
        return -1
    return deque[0]

def back():
    if not deque:
        return -1
    return deque[-1]

for _ in range(int(input())):
    input_data = sys.stdin.readline().split()
    if input_data[0] == 'push':
        push(input_data[1])
    if input_data[0] == 'front':
        print(front())
    if input_data[0] == 'empty':
        print(empty())
    if input_data[0] == 'back':
        print(back())
    if input_data[0] == 'pop':
        print(pop())
    if input_data[0] == 'size':
        print(size())







