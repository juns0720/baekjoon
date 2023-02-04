import sys
input = sys.stdin.readline


stick = list(input().rstrip())

Stack = []
count = 0
last = 0
for i in range(0,len(stick)):
    if stick[i] == '('and stick[i+1] !=')':
            if stick[i] =='(':
                  count+=1
                  last+=1

    elif stick[i] == '('and stick[i+1] ==')':
        last+=count

    elif i != (len(stick)-1):
        if stick[i] == ')'and stick[i-1] !='(':
            count-=1

print(last)
          

            






