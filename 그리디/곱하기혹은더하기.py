S = input()

result = int(S[0])

for i in range(1, len(S)):
    if S[i] == '1' or S[i] == '0' or result == 0 or result == 1:
    #if S[i] <= 1 or result <= 1:   <- 이것도 가능 결국은 1보다 같거나 작은 경우니까
        result += int(S[i])
    else:
        result = result * int(S[i])

print(result)

"""
02984


567
"""