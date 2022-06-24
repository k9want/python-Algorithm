data = list(input())
data.sort()

alpha = []
numbers = []
for d in data:
    if d.isdigit():
        numbers.append(int(d))
    else:
        alpha.append(d)

alpha.sort()
sum_value = sum(numbers)
alpha.append(str(sum_value))

print(''.join(alpha))
"""
K1KA5CB7

AJKDLSI412K4JSJ9D
"""