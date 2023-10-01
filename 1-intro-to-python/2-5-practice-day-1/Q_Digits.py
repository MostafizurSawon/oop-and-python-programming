n = int(input())

while n > 0:
    tmp = input()
    tmp = tmp[::-1]
    for i in tmp:
        print(i, end=' ')
    print(end='\n')
    n = n-1


# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Q
