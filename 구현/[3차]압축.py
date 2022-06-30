
def solution(msg):
    data = dict()
    for i in range(ord('A'), ord('Z' ) +1):
        data[chr(i)] = i - ord('A') + 1

    idx = 27
    start = 0
    end = 1
    answer = []

    while end < len(msg ) +1:
        s = msg[start: end]
        if s in data:
            end += 1
        else:
            answer.append(data[s[:-1]])
            data[s] = idx
            idx += 1
            start = end -1
    answer.append(data[s])
    return answer
