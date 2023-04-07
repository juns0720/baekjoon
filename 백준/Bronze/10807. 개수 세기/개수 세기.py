
N = int(input())
a = list(map(int,input().split()))
cnt = 0
t = int(input())
for i in range(N):
    if a[i] == t:
        cnt+=1
print(cnt)