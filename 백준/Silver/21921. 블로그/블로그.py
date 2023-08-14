import sys
input = sys.stdin.readline

N,X = map(int,input().split())
visit = list(map(int,input().split())) 
res = [sum(visit[0:X]),1]
prev = 0
tmp = res[0]
for next in range(X,N):
    tmp += (visit[next]-visit[prev])
    if tmp > res[0]:
        res[0] = tmp
        res[1] = 1
    elif tmp == res[0]:
        res[1]+=1
    prev+=1


if res[0] == 0:
    print("SAD")
else:
    for i in res:
        print(i)