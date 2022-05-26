def solution(n):
    answer = ''
    nums = ['4', '1', '2']
    while n:
        answer = nums[n % 3] + answer
        n = n // 3 - (n % 3 == 0)

    return answer