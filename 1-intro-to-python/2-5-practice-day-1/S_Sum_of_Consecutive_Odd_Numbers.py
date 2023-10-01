# n = int(input())

# while n > 0:
#     a, b = map(int, input().split())
#     sum = 0
#     for i in range(min(a, b)+1, max(a, b)):
#         if i % 2 == 1:
#             sum += i
#     print(sum)
#     n = n-1

# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/S


n = int(input())

while n > 0:
    a = int(input())
    b = int(input())
    min = min(a, b)
    max = max(a, b)
    # for i in range(min+1, max):
    #     if i % 2 == 1:
    #         print(i, end=" ")
    # print("\n")
    print(min, max)
    n = n-1
