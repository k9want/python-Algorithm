def solution(s):
    answer = ''

    nums = list(map(int, s.split(' ')))

    return str(min(nums)) + " " + str(max(nums))