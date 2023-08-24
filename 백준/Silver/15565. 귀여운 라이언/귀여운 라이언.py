import sys
input = sys.stdin.readline

N,K = map(int,input().split())
arr = list(map(int,input().split()))
s = 0
e = 0
cnt = 0
res = N+1
while e < N:
        if cnt < K:
            if arr[e] == 1:
                cnt+=1
            if cnt != K:
                e+=1
        else: 
            res = min(res,e-s+1)
            if arr[s] == 1:
                e+=1
                cnt-=1
            s+=1
if res == N+1:
    print(-1)
else:
    print(res)