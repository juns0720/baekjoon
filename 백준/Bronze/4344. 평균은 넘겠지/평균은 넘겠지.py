import sys
input = sys.stdin.readline

case = int(input())


for i in range(case):
 sum = 0
 avg = 0
 cnt = 0
 score=list(map(int,input().split()))
 for i in range(len(score)-1):
        sum += score[i+1]
 avg = sum/score[0]
 for i in range(score[0]):
        if score[i+1] > avg :
            cnt+=1 
 print(f"{cnt/score[0]*100 :.3f}%")
