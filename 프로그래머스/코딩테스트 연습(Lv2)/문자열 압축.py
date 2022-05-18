"""
(1) 1개부터 문자열 길이까지 순서대로 1씩 증가시키면서 탐색
(2) 문자열 비교를 위에 같으면 같은 개수만큼 cnt 증가
(3)다르면 비교할 문자를 새로 갱신
(4) min으로 비교할 떄 아무리 커도 len(s) 원래 문자열보단 클수 없기 때문에 해당 문자와 비교해서 최솟값을 찾고 반환하도록 코드 작성했다.

생각한대로 구현해서 뿌듯했음...
"""
def solution(s):
    answer = len(s)

    for i in range(1, len(s)):
        j = 0
        result = ''
        cnt = 1
        while True:
            if j > len(s):
                break
            d1 = s[j:j + i]
            j = j + i
            d2 = s[j:j + i]
            if d1 == d2:
                cnt += 1
            else:
                if cnt == 1:
                    result += d1
                else:
                    result += str(cnt)
                    result += d1
                    cnt = 1

        # print(result)
        answer = min(answer, len(result))

    return answer