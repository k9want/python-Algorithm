#전부 1로 만드는 경우와 0으로 만드는 경우 중 최솟값을 출력
s = input()

cnt0 = 0
cnt1 = 0

if s[0] == '1':
    cnt0 += 1
else:
    cnt1 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            cnt0 += 1
        elif s[i+1] == '0':
            cnt1 += 1

print(min(cnt0, cnt1))

"""
0001100

0101100
1101100
"""
