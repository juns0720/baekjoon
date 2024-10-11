import sys
input = sys.stdin.readline

D,K = map(int,input().split())

for i in range(K-1,-1,-1):
    now = K
    prev = i
    cnt = 1
    while True:
        if cnt == D:
            print(now)
            print(now+prev)
            exit()
        if now < prev or prev == 0:
            break
        tmp = now-prev
        now = prev
        prev = tmp
        cnt+=1


