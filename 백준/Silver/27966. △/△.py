import sys
input = sys.stdin.readline

N = int(input())

res = N-1
for i in range(N,1,-1):
    res += 2*(i-2)
print(res)
for i in range(2,N+1):
    print(1,i)