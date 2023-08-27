import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
nl = ['0' for _ in range(N)]
for i in range(len(arr)):
    j = 0
    M = arr[i]
    cnt = 0
    while True:
        if cnt > M-1:
                if nl[j] == '0':
                    nl[j] = str(i+1)
                    break       
        else:
            if nl[j] == '0':
                cnt+=1 
        j+=1
print(' '.join(nl))
