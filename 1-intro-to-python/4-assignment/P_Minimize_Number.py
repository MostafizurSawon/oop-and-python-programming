n = int(input())
list = list(map(int, input().split()))
b = list[:]

count = False
ind = -1

while count == False:
    for i, x in enumerate(list):
        if ind != -1:
            continue
        if list[i] % 2 == 0:
            list[i] = x/2

        else:
            ind = i
    if ind != -1:
        count = True

# print(list, b)
ans = 0
while True:
    if b[ind] != list[ind]:
        list[ind] = list[ind]*2
        ans += 1
    else:
        break

print(ans)
