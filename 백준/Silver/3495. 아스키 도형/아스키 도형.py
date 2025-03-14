import sys
input = sys.stdin.readline

h,w = map(int,input().split())

board = [list(input().strip()) for _ in range(h)]

stack = []
res = 0
for row in board:
    cnt = 0
    for col in row:
        if col == '/':
            if stack and stack[0] in ['/','\\']:
                stack.pop()
                res += (1 + cnt)
                cnt = 0
            elif not stack:
                stack.append(col)
        elif col == '\\':
            if stack and stack[0] in ['/','\\']:
                stack.pop()
                res += (1 + cnt)
                cnt = 0
            elif not stack:
                stack.append(col)
        else:
            if stack:
                cnt += 1
print(res)