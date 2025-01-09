import sys
input = sys.stdin.readline
N = int(input())

cnt = 0

for i in range(N):
    stack = []
    word = list(input().strip())
    for s in word:
        if not stack:
            stack.append(s)
        else:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
    if not stack:
        cnt+=1
print(cnt)