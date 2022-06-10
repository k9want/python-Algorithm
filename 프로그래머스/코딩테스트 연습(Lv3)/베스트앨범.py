"""
해시정렬은 sorted(dict.items(), key= lambda x : x[1])
이것처럼 items()를 사용할 것

주의 장르별 두개씩 모아 베스트 앨범 출시
"""


def solution(genres, plays):
    answer = []
    data = dict()
    # 뭐가 더 많이 재생됐니??
    play = dict()
    for i in range(len(genres)):
        if genres[i] in play.keys():
            play[genres[i]] += plays[i]
        else:
            play[genres[i]] = plays[i]
        data[(genres[i], i)] = plays[i]

    play_cnt = sorted(play.items(), key=lambda x: -x[1])
    sorted_data = sorted(data.items(), key=lambda x: (-x[1], x[0][1]))
    # print(sorted_data)
    # print(play_cnt)
    for pc in play_cnt:
        cnt = 0
        for i in range(len(sorted_data)):
            if cnt == 2:
                break
            if pc[0] == sorted_data[i][0][0]:
                answer.append(sorted_data[i][0][1])
                cnt += 1
        # print(pc[0])

    return answer