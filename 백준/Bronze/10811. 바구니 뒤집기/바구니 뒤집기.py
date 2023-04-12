import sys
input = sys.stdin.readline

N,M = map(int,input().split())

ball = [str(i) for i in range(1,N+1)]
for _ in range(M):
    i,j = map(int,input().split())
    dis = (j-i+1)//2
    i-=1
    j-=1
    for t in range(0,dis):
        tmp = ball[i+t]
        ball[i+t] =ball[j-t]
        ball[j-t] = tmp
print(' '.join(ball))
