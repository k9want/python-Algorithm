n = list(map(int, input()))

middle = len(n)//2

left = 0

right = 0
for i in range(middle):
    left += n[i]


for i in range(middle, len(n)):
    right += n[i]

if left == right:
    print("LUCKY")
else:
    print("READY")