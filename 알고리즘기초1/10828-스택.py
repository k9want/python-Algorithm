import sys
input = sys.stdin.readline

n = int(input())
stk = []



def push(x):
    stk.append(x)

def pop():
    if(not stk):
        return -1
    return stk.pop()

def size():
    return len(stk)

def empty():
    if (not stk):
        return 1
    return 0

def top():
    if(not stk):
        return -1
    return stk[-1]



for _ in range(n):
    input_data = input().split()
    command = input_data[0]

    if command == 'push':
        push(input_data[1])
    if command == 'pop':
        print(pop())
    if command == 'size':
        print(size())
    if command == 'empty':
        print(empty())
    if command == 'top':
        print(top())







