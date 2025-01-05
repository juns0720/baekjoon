import sys
input = sys.stdin.readline

tc = 1
while True:
    stack = []
    cnt = 0
    s1 = input().strip()

    if '-' in s1:
        break

    for i in s1:
        if i == "{":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                cnt+=1
                stack.append('{')
    
    cnt+= len(stack)//2
        
    print(f'{tc}. {cnt}')
    tc+=1