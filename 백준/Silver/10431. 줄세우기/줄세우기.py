import sys
input = sys.stdin.readline

P = int(input())
c_list = [ list(map(int,input().split())) for _ in range(P)]

for i in range(0,P):
    cnt = 0
    for j in range(2,21):
        tmp = c_list[i][j]
        for k in range (j-1,0,-1):
            if c_list[i][k] > c_list[i][j] :
                cnt+=1
            if c_list[i][j] < c_list[i][j] or j == 1:
                c_list[i][j] = c_list[i][k]
                c_list[i][k] = tmp
                break
    print(i+1,cnt)