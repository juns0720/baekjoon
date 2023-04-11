n = int(input())
cnt = 1
i = 6
while n > 1:
    n-=i
    i+=6
    cnt+=1
print(cnt)