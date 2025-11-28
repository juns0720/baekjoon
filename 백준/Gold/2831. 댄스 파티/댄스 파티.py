import sys
input = sys.stdin.readline

N = int(input())
lm,hm = [],[]
for i in list(map(int,input().split())):
    if i < 0:
        lm.append(-i)
    else:
        hm.append(i)

lwm,hwm = [],[]
for i in list(map(int,input().split())):
    if i < 0:
        lwm.append(-i)
    else:
        hwm.append(i)

cnt = 0

lm.sort()
hm.sort()
lwm.sort()
hwm.sort()
i,j = 0,0
while i < len(lm) and j < len(hwm):
    if lm[i] > hwm[j]:
        cnt += 1
        i += 1
        j += 1
    else:
        i += 1

i,j = 0,0
while i < len(lwm) and j < len(hm):
    if lwm[i] > hm[j]:
        cnt += 1
        i += 1
        j += 1
    else:
        i += 1
        
print(cnt)