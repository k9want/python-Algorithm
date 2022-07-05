def solution(s):
    answer = True

    p = 0
    y = 0

    data = s.lower()

    for d in data:
        if d == "p":
            p += 1
        elif d == 'y':
            y += 1
    if p != y:
        return False

    return True