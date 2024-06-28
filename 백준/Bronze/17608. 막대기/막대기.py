import sys
input = sys.stdin.readline

n = int(input())

stack = []

for i in range(n):
    stack.append(int(input()))
cnt = 1
max_height = stack.pop()
while stack:
    current_height = stack.pop()
    if max_height < current_height:
        max_height = current_height
        cnt+=1
print(cnt)