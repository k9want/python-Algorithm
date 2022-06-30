"""
짝수는 +1
홀수는 마지막 최하위 0비트 자릿수를 구하고 그 자리와 바로 다음 자리를 10으로 바꾸고 그 수를 십진수로 바꿔서 출력한다.
"""
def solution(numbers):
    answer = []

    for num in numbers:
        bin_num = bin(num)
        tmp = '0' + bin_num[2:]

        lastZero = -1
        for i in range(len(tmp)):
            if tmp[i] == '0':
                lastZero = max(lastZero, i)

        if num % 2 == 0:
            answer.append(num + 1)
        else:
            result = tmp[:lastZero] + '10' + tmp[lastZero + 2:]
            answer.append(int(result, 2))

    return answer