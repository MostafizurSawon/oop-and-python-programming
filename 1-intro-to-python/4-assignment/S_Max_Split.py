s = input()
list = []
r = 0
l = 0
ans = ""

for c in s:
    if c == 'L':
        l += 1
        ans += c

    elif c == 'R':
        r += 1
        ans += c
    if r == l and r != 0:
        list.append(ans)
        ans = ans[:0]
        r = 0
        l = 0

print(len(list))
for i in list:
    print(i)


