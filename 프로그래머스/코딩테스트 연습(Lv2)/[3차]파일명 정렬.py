"""
정렬 조건은 정렬할 때 key에다가 기준으로 맞추면 된다.!
처음부터 head, number, tail에 맞출 생각을 하지 말것
결과는 원래의 값을 합쳐서 출력해야하기때문에 변환 과정이라면 적용해도 되지만 변환과정이 아닌 정렬과정이기 때문에 정렬할 때 고려할 것

핵심!!
head, number, tail 이 부분을 나누는 것이 중요
head와 number를 나누는 기준 num_check이라는 변수를 이용한다.
tail은 number는 tail을 나누는 것은 문자가 처음 나올 때
- 따라서 else:부분에서 나머지 부분을 전부 쓸어담고 break한다. (tail에도 숫자가 나올수 있다고 문제에서 명시했기 때문에)
"""

def solution(files):
    answer = []

    for file in files:
        head, number, tail = '', '', ''

        num_check = False
        for i in range(len(file)):
            if file[i].isdigit():
                num_check = True
                number += file[i]
            elif not num_check:
                head += file[i]
            else:
                # 중요한 것은 file[i:] <- 이 부분!!!
                tail += file[i:]
                break

        answer.append((head, number, tail))
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))

    # print(answer)

    return [''.join(a) for a in answer]