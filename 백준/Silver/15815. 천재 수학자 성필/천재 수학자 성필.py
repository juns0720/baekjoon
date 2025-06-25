import sys
input = sys.stdin.readline

arr = list(input().strip())

def cal(op,n1,n2):
    if op == "+":
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 // n2
stack = []

for i in range(len(arr)):
    s = arr[i]
    if ord('0') <= ord(s) <= ord('9'):
        stack.append(int(s))
    else:
        n2 = stack.pop()
        n1 = stack.pop()
        stack.append(cal(s,n1,n2))
print(stack[0])