"""
아이디어
각각의 순위를 rank 리스트로 만들고
로또 번호 리스트에 count(0)을 통해서 0개수를 파악
그에 맞게 최고 순위와 최저순위를 출력한다.
"""


def solution(lottos, win_nums):
    rank_list = [6, 6, 5, 4, 3, 2, 1]
    result = 0

    zero_cnt = lottos.count(0)

    for l in lottos:
        if l in win_nums:
            result += 1

    answer = [rank_list[result + zero_cnt], rank_list[result]]
    return answer