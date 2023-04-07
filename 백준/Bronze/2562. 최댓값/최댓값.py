import sys
input = sys.stdin.readline

list1 = []
cnt = 0
for i in range(9):
    list1.append(int(input()))
for i in list1:
    cnt+=1
    if max(list1) == i:
        break

print(max(list1))
print(cnt)
