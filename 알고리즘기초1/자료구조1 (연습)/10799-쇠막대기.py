input_data = input().rstrip()

stk = []
result = 0
for i in range(len(input_data)):
    if input_data[i] == '(':
        stk.append(input_data[i])
    else:
        if input_data[i-1] == '(':
            stk.pop()
            result += len(stk)
        else:
            stk.pop()
            result += 1

print(result)