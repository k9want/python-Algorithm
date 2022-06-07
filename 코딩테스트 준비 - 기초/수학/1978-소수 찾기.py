"""
소수는 1과 자기자신을 제외한 어떤 수도 나눠 떨어지지 않는 수
"""
import math
n = int(input())

data = list(map(int,input().split()))

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
cnt = 0
for d in data:
    if is_prime(d):
        cnt += 1

print(cnt)