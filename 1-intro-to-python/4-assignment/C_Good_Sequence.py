from collections import Counter

n = int(input())
x = list(map(int, input().split()))
# print(x)
ans = 0

list = Counter(x)
# print(list)

for a, b in list.items():
    # print(a, b)
    if a <= b:
        ans += b-a
    else:
        ans += b

print(ans)

# list.sort()
# ans = 0

# for c in list:
#     co = list.count(c)
#     # print(c, co)
#     if c == 0:
#         continue
#     # print(c)
#     if (c < co):
#         ans += (co-c)
#         list.remove(c)
#     elif c != co:
#         ans += co
#         list.remove(c)
#     # print(c, co)

# print(ans)


# N = int(input())
# a = list(map(int, input().split()))

# C = Counter(a)
# print(a)
# ans = 0
# for x, y in C.items():
#     print(x, y)
#     if x <= y:
#         ans += (y-x)
#     else:
#         ans += y
# print(ans)
