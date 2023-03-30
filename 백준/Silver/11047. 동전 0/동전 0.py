import sys
input = sys.stdin.readline

N,k = map(int,input().split())
coin = []
cnt = 0
error = False
for i in range(N):
    coin.append(int(input()))
coin.reverse()
for i in coin:
    if k == 0:
        break
    if k >= i:
        cnt +=k // i
        t = k//i
        k -=t*i
print(cnt)


