import sys
input = sys.stdin.readline

n = int(input())

lstB = list(map(int,input().split()))
lstB.sort(reverse = True)
cnt = 0

while lstB[0] > 0:
    for i in range(n):
        if lstB[i] % 2 == 1:
            lstB[i]-=1
            cnt+=1
    if lstB[0] == 0:
        break

    for i in range(n):
        lstB[i] >>= 1
    cnt+=1
for i in range(n):
    cnt+=lstB[i]
print(cnt)