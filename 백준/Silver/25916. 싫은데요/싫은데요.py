import sys
input = sys.stdin.readline

#N,M = 8,10
#Hole = [2,2,2,2,11,2,5,2]
N,M = map(int,input().split())
Hole = list(map(int,input().split()))
Sum = 0
Max_Area = 0
jump = False
jump_i = 0
i = 0
t = 0
while t < N:
    if Sum+Hole[i] > M:
        Max_Area = max(Sum,Max_Area)
        Sum = 0
        if Hole[i] > M:
            t = i
            i = t
        else:
            t+=1
            i = t
    else:
        Sum+=Hole[i]
    i+=1
    if i > N-1:
        Max_Area = max(Sum,Max_Area)
        t+=1
        i = t
        break
print(Max_Area)

    