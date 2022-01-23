from itertools import combinations

data = []

for _ in range(9):
    data.append(int(input()))
    data.sort()

result = list(combinations(data, 7))

for res in result:
    if (sum(res) == 100):
        for r in res:
            print(r)

        break
