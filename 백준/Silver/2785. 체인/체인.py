import sys
input = sys.stdin.readline

N = int(input())
chains = list(map(int,input().split()))

chains.sort()
start = 0
end = N-1
cnt = 0
while start != end:
    if chains[start] > 0:
        chains[start]-=1
        end-=1
        cnt+=1
    else:
        start+=1
print(cnt)