import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    n = int(input())
    score = []
    cnt = 1

    for i in range(n):
        score.append(list(map(int,input().split())))
    score.sort()

    min = score[0][1]

    for i in range(1,n):
        if score[i][1] < min:
            cnt+=1
            min = score[i][1]
    print(cnt)
 

