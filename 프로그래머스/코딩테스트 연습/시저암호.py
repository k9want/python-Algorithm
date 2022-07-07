def solution(s, n):
    data = list(s)

    for i in range(len(data)):
        if data[i].isupper():
            data[i] = chr((ord(data[i]) - ord('A') + n) % 26 + ord('A'))
        elif data[i].islower():
            data[i] = chr((ord(data[i]) - ord('a') + n) % 26 + ord('a'))

    return "".join(data)