n = 9
data = [int(input()) for _ in range(9)]
data.sort()

total = sum(data)

data.sort()
finish = False
for i in range(0, n):
    for j in range(i + 1, n):
        if total - data[i] - data[j] == 100:
            a = data[i]
            b = data[j]
            data.remove(a)
            data.remove(b)
            finish = True
            break
    if finish:
        break

# 출력 1
# for d in data:
#     print(d)


# 출력2
# print('\n'.join(map(str, data)))

