cnt = 0
for _ in range(int(input())):
    if int(input().strip()[2:]) < 91:   
        cnt+=1
print(cnt)