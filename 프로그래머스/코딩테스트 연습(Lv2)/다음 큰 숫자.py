"""
- bin()[2:]
- 문자열.count('개수를 찾고자하는 문자')
"""
def solution(n):
    m = bin(n)[2:]
    while True:
        n += 1
        if m.count('1') == bin(n)[2:].count('1'):
            break

    return n