import sys
input = sys.stdin.readline
N,K,M = map(int,input().split())
arr = [i for i in range(1,N+1)]
num = K-1
print(arr.pop(num),end=' ')
cnt = 1
while arr:
    if cnt // M % 2 == 0:
        num = (num+(K-1))%len(arr)
    else:
        num = num-K
        num%=len(arr)
    print(arr.pop(num),end=' ')
    cnt+=1