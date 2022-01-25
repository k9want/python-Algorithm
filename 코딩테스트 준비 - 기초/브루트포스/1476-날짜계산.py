def cal(n, m, k):
    i = 1
    while True:
        if i % 15 == n and i % 28 == m and i % 19 == k:
            print(i)
            break
        i += 1


    return i

n, m, k = map(int,input().split())
if n == 15:
    n = 0
if m == 28:
    m = 0
if k == 19:
    k = 0
cal(n,m,k)

# def cal(n, m, k):
#     i = 1
#     while True:
#         if i % 15 == n:
#             if i % 28 == m:
#                 if i % 19 == k:
#                     break
#         i += 1
#
#
#     return i
#
#
# n, m, k = map(int,input().split())
# if n == 15:
#     n = 0
# if m == 28:
#     m = 0
# if k == 19:
#     k = 0
# print(cal(n,m,k))