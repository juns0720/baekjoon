n,m = map(int,input().split())
ball = ['0' for _ in range(0,n)]
for _ in range(m):
    i,j,k = map(int,input().split())
    for t in range(i,j+1):
        ball[t-1] = str(k)
print(' '.join(ball))
