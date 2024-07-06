import sys
input = sys.stdin.readline

s1 = input().strip()
stack = []

for str in s1:
    if str == '(':
        stack.append(str)
    elif str == ')':
        while stack and stack[-1] != '(':
            print(stack.pop(),end='')
        stack.pop()

    elif str == '*' or str == '/':
        while stack and  (stack[-1] == '*' or stack[-1] == '/'):
            print(stack.pop(), end='')
        stack.append(str)

    elif str == '+' or str == '-':
        while stack and stack[-1] != '(':
            print(stack.pop(),end='')
        stack.append(str)

    else:
        print(str,end='')

while stack:
    print(stack.pop(),end='')