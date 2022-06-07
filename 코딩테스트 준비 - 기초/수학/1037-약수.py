cnt = int(input())
data = list(map(int,input().split()))

#data에는 모든 약수가 있다.
# 가장 작은 값과 가장 큰 값을 곱하는 것으로 답을 구한다.

data.sort()
print(data[0] * data[-1])