"""
행렬의 성질 이용 arr1의 col 과 arr2 row가 같아야 곱할 수 있다.
"""
def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]

    for y1 in range(len(arr1)):
        for x1 in range(len(arr1[0])):
            for x2 in range(len(arr2[0])):
                # print(arr1[y1][x2], arr2[x1][x2])
                answer[y1][x2] += (arr1[y1][x1] * arr2[x1][x2])

    print(answer)

    return answer