import sys
n1,n2 = map(int,input().split())


arr = []
for s in list(reversed(input().strip())):
    arr.append((s,0))

for s in list(input().strip()):
    arr.append((s,1))

for _ in range(int(input())):
    i = 0
    while i < len(arr)-1:
        if arr[i][1] == 0 and arr[i+1][1] == 1:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            i+=1
        i+=1

for i in arr:
    print(i[0], end = '')