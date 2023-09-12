n = int(input())
cnt = 0
i = 1
while n > 0:
    n-=i
    cnt+=1
    i+=1
if n < 0:
    cnt-=1
print(cnt)