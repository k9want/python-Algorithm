"""
문제를 보면 입장, 변경 때 닉네임을 바꿀수 있다.
그리고 마지막에는 최종 변경된 닉네임으로 출력이 되기 때문에
id를 이용해서 key 닉네임을 value로 하는 사전 자료형으로 유저아이디와 닉네임을 저장하고
상황에 맞게 출력하도록 코드를 작성했다.
"""
def solution(record):
    data = dict()

    for r in record:
        re = r.split()
        # print(re)
        if re[0] == 'Enter':
            data[re[1]] = re[2]
        elif re[0] == 'Change':
            data[re[1]] = re[2]

    answer = []

    for r in record:
        re = r.split()
        if re[0] == 'Enter':
            answer.append(data[re[1]] + "님이 들어왔습니다.")
        elif re[0] == 'Leave':
            answer.append(data[re[1]] + "님이 나갔습니다.")

    return answer