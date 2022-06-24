# n = list(map(int, input()))
#
# middle = len(n)//2
#
# left = 0
#
# right = 0
# for i in range(middle):
#     left += n[i]
#
#
# for i in range(middle, len(n)):
#     right += n[i]
#
# if left == right:
#     print("LUCKY")
# else:
#     print("READY")


n = input()

length = len(n)
mid = length // 2
cnt = 0
left = 0
right = 0

for s in n:
    if cnt < mid:
        right += int(s)
    else:
        left += int(s)
    cnt += 1

if left == right:
    print("LUCKY")
else:
    print("READY")