import sys
input = sys.stdin.readline

n,t = map(int,input().split())

c = [list(map(int,input().split())) for _ in range(n)]
c.sort(key = lambda x :(-x[1], -x[0]))

res = 0
for i in range(n):
    res += (c[i][0] + c[i][1]*(t-i-1))
print(res)