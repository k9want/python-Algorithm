"""
폰 번호별 거리를 구할 수 있는 함수를 구현
 각각의 좌표를 사전 자료형으로 설정하고
 거리를 구한 뒤 그에 맞는 손을 return 하는 함수를 만들고

 2,5,8,0일 때마다 해당 함수를 실행

매순간 왼손의 위치와  오른손의 위치가 달라질때마다 갱신하고 거리를 계산할 때 사용
"""
def next_hand(left, right, now_number, hand):
    phone = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    distance_l = abs(phone[left][0] - phone[now_number][0]) + abs(phone[left][1] - phone[now_number][1])
    distance_r = abs(phone[right][0] - phone[now_number][0]) + abs(phone[right][1] - phone[now_number][1])

    print(distance_l)
    print(distance_r)

    if distance_l > distance_r:
        return 'R'
    elif distance_l < distance_r:
        return 'L'
    else:
        if hand == 'left':
            return 'L'
        else:
            return 'R'


def solution(numbers, hand):
    answer = ''

    l_num = [1, 4, 7]
    r_num = [3, 6, 9]
    left = '*'
    right = '#'

    for n in numbers:
        if n in l_num:
            answer += 'L'
            left = n
        elif n in r_num:
            answer += 'R'
            right = n
        else:
            middle = next_hand(left, right, n, hand)
            answer += middle
            if middle == 'L':
                left = n
            else:
                right = n

    return answer