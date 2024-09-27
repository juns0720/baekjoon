import sys
input = sys.stdin.readline

for tc in range(1,int(input())+1):
    m = int(input())
    time = [list(map(int,input().split())) for _ in range(m)]
    time.sort(key = lambda x:(x[0],x[2]))
    cnt = 0
    prev = 0 
    day = 1
    for i in range(m):
        if day < time[i][0]:
            day+=1
            prev = 0
        if time[i][1] >= prev:
            prev = time[i][2]
            cnt+=1
    print("Scenario #"+str(tc)+":")
    print(cnt)
    print()
