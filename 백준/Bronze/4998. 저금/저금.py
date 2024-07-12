import sys
input = sys.stdin.readline


while True:
    try:
        N,B,M = map(float,input().split())
    except:
        exit()
    cnt = 0
    B *=0.01
    while N < M:
        N+= (N*B)
        cnt+=1
    print(cnt)