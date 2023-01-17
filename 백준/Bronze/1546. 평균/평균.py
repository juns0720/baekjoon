import sys
input = sys.stdin.readline

num = int(input())
score = list(map(int,input().split()))
avg = 0
for i in range(num) :
 avg += score[i]/max(score)*100

print(f"{avg / num}")
