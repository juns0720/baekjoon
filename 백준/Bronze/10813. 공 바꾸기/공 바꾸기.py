import sys
input = sys.stdin.readline

N,M = map(int,input().split())

ball = [str(i) for i in range(1,N+1)]
for _ in range(M):
    i,j = map(int,input().split())
    i-=1
    j-=1
    temp = ball[i]
    ball[i] = ball[j]
    ball[j] = temp
print(' '.join(ball))
