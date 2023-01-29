import sys
input = sys.stdin.readline
Stack = []

def s_push(x):
    Stack.append(x)

def s_pop():
    if len(Stack) == 0:
        return -1
    else:
        a = Stack[-1]             #1이랑 2 들어가있으면? 길이는 2
        del Stack[-1]
        return a

def s_size():
    size = (len(Stack))
    return size

def s_empty():
    if len(Stack) == 0:
        return 1
    else:
        return 0
    
def s_top():
    if len(Stack) == 0:
        return -1
    else:
        top = (Stack[-1])
        return top

n = int(input())

for i in range(n):
    o = []
    o.append(list(map(str,input().split())))
    if len(o[0]) >= 2 :             #push
        s_push(o[0][1])      

    elif o[0][0] == 'pop':          #pop
        pop = s_pop()      
        print(pop)
    elif o[0][0] == 'size':         #size
        size = s_size()      
        print(size)
    elif o[0][0] == 'empty':        #empty
        empty = s_empty()      
        print(empty)
    elif o[0][0] == 'top':          #top
        top = s_top() 
        print(top)

