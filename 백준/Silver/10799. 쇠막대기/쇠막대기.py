import sys
input = sys.stdin.readline


str = (input().rstrip())
str = str.replace('()','1')
stick = list(str)
Stack = []
last = 0

for i in range(0,len(stick)):
    if stick[i] =='(':
        Stack.append('(')
        last+=1
    elif stick[i] == '1':
        last +=int(len(Stack))
    elif stick[i] ==')':
        Stack.pop()
        
print(last)
          
