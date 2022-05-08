#나의 풀이
def solution(s):
    word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    eng = []
    result = []
    for i in s:
        if i.isdigit():
            result.append(str(i))
        else:
            eng.append(i)
            w = ''.join(eng)
            if w in word:
                result.append(str(word.index(w)))
                eng = []

    answer = int(''.join(result))
    return answer

#다른 유저들 풀이 (1) 리스트 사용
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)

#다른 유저들 풀이 (2) 사전형 dict 사용
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)