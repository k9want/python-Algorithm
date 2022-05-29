"""
규칙 찾기
math gcd() 최대공약수
"""
import math


def solution(w, h):
    answer = 1

    if w == 1 or h == 1:
        answer = 0
    elif w == h:
        answer = (w * w) - w
    else:
        answer = (w * h) - ((w + h) - math.gcd(w, h))

    return answer