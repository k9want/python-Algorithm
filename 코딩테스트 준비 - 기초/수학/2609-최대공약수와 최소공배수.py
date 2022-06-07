"""
두수의 최소공배수는 두수의 곱 나누기 두수의 최대공약수
"""
import math
a, b = map(int,input().split())


print(math.gcd(a, b))
print(a * b // math.gcd(a,b))