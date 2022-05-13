"""
대기트럭을 queue로
그리고 다리를 queue로 만들고
다리의 트럭무게를 계속 계산하면서 대기트럭의 첫번째와 비교후 가능하면 다리에 올리고
안 되면 0으로 해서 트럭이 건너는 코드를 작성했다.
"""
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    now_weight = 0
    while bridge:
        now_weight -= bridge.popleft()
        answer += 1
        if trucks:
            if now_weight + trucks[0] <= weight:
                now_weight += trucks[0]
                bridge.append(trucks.popleft())
            else:
                bridge.append(0)

    return answer