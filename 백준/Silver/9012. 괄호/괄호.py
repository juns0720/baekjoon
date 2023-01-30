import sys
input = sys.stdin.readline

def pop(Stack,t):

    if len(Stack) == 0:
        return -1
    elif len(Stack) < 2:
        return
    else:       
        del Stack[t]
        del Stack[t-1]
   
    if len(Stack) >= 2:
        for i in range(1,(len(Stack))):
            if i < len(Stack):
                if Stack[i-1] == '(':
                    if Stack[i] == ')':
                        pop(Stack,i)
    elif len(Stack) < 2:
        return
   
    
def Vps(list):
   if len(list) >= 2:
        for i in range(1,(len(list))):
            if i < len(list):
                if list[i-1] == '(':
                    if list[i] == ')':
                        pop(list,i)

   if len(list) >= 1:
       print('NO')
   elif len(list) == 0:
       print('YES')





n = int(input())

for i in range(n):
    str1 = []
    a = input().rstrip()
    str1 = list(a)
    Vps(str1)
