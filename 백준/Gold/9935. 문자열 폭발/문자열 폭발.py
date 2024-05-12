import sys
input = sys.stdin.readline

s1 = list(input().strip())
s2 = input().strip()

stack = []
s2_length = len(s2)

for i in range(len(s1)):
    stack.append(s1[i])
    if ''.join(stack[-s2_length:]) == s2:
        for _ in range(s2_length):
            stack.pop()
res = ''.join(stack)
print("FRULA" if res == '' else res)