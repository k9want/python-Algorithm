# 9012-괄호 stk이용
for _ in range(int(input())):
    result = True
    input_data = input()
    stk = []
    for i in input_data:
        if i == '(':
            stk.append(i)
        else:
            if stk:
                stk.pop()
            else:
                result = False
                break

    if stk:
        result = False

    print('YES' if result else 'NO')




