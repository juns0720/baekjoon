import sys
input = sys.stdin.readline



while 1:
    t = input().rstrip()
    Stack = []

    if t == '.':
        break

    for i in t:
        if i == '[' or i == '(':
            Stack.append(i)
        elif i == ']':
            if len(Stack) != 0 and Stack[-1] == '[':
                Stack.pop()
            else:
                Stack.append(']')
                break
                
        elif i == ')':
            if len(Stack) != 0 and Stack[-1] == '(':
                Stack.pop()
            else:
                Stack.append(')')
                break
    if len(Stack) == 0:
        print('yes')
    else:
        print('no')
