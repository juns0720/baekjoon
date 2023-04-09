import math
N = int(input())
Nl =list(map(int,input().split()))
cnt = 0
for j in Nl:
    res = True
    for i in range(2,int(math.sqrt(j))+1):
        if j % i == 0:
            res = False
            break
    if j != 1 and res == True:
        cnt+=1
print(cnt)
            
    