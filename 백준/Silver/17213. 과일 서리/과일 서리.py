import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

def fac(n):
    if n < 2:
        return 1
    
    return n*fac(n-1)


if N == 1 or N == M:
    print(1)
    exit()
if N == 2:
    print(M-1)
    exit()

n,r = M-1,M-N
r = min(r,n-r)
res = 1

for i in range(n,n-r,-1):
    res*= i
print(res//fac(r))