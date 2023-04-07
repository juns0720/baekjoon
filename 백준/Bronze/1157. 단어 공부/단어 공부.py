import sys
input = sys.stdin.readline

s = input().strip().lower()
check =list(set(s))
list1 = []
for i in check:
    list1.append([s.count(i),i])
list1.sort(reverse = True)
if len(list1) == 1:
    print(list1[0][1].upper())
else:
    if list1[0][0] == list1[1][0]:
        print("?")
    else:
        print(list1[0][1].upper())
