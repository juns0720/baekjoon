import sys
input = sys.stdin.readline

N,K = map(int,input().split())

seq = list(map(int,input().split()))
num = [0 for _ in range(200001)]
s,e = 0,0
num[seq[e]]+=1
Max = 0
while s < len(seq):
    if num[seq[e]] > K:
        Max = max(e-s,Max)
        num[seq[s]]-=1
        s+=1
    else:
        if e == len(seq)-1:
            Max = max(e-s+1,Max)
            num[seq[s]]-=1
            s+=1
        else:
            e+=1
            num[seq[e]]+=1
print(Max)