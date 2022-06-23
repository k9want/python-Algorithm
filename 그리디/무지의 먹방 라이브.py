"""
heap을 이용해서 시간이 적게 걸리는 음식부터 확인 (시간을 기준으로 정렬)
k보다 작으면 다 먹은 거니까 -1
아니면 k보다 커지기 전까지 음식을 뺀다.
"""


import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야한다. 우선순위 큐를 사용
    q = []
    for i in range(len(food_times)):
        # (시간, 번호)
        heapq.heappush(q, (food_times[i], i + 1))

    # 먹는데 총 걸린 시간
    sum_value = 0
    # 이전에 먹다만 시간  -> 이전 음식이 더 시간이 적게 걸리기 때문에 이전 음식들 먹는데 걸렸던 시간만큼 빼고 추가로 먹는걸 계산하기 위해 사용
    previous = 0
    length = len(food_times)  # 남은 음식 개수

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    # 번호로 정렬
    result = sorted(q, key=lambda x: x[1])

    return result[(k - sum_value) % length][1]