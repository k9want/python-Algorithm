"""
시간복잡도
-중복없이 따라서 N! 가능
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []
visited = [False] * (n+1)

def recur(num):
    if num == m:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n+1):
        if visited[i] == False:
            visited[i] = True
            result.append(i)
            recur(num+1)
            result.pop()
            visited[i] = False

recur(0)