"""
이분탐색의 핵심!!
어떤 것을 범위로 할지
어떤 것을 탐색기준으로 세울지
"""
def solution(n, times):
    answer = 0

    left = min(times)
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            people += (mid // time)

            # 왜냐?! n이상이라는 것이므로 right를 mid - 1을 하면되는 것
            if people >= n:
                break

        if people >= n:
            answer = mid
            right = mid - 1
        elif people < n:
            left = mid + 1

    return answer