"""
a, b의 최소공배수 = a * b // gcd(a, b)
두 수의 최소공배수는 두 수의 곱을 두 수의 최대공약수로 나눈 수
"""

import math


def solution(arr):
    answer = 0
    for i in range(1, len(arr)):
        arr[i] = arr[i - 1] * arr[i] // (math.gcd(arr[i - 1], arr[i]))

    return arr[-1]