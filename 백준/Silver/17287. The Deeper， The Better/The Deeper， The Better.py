import sys
input = sys.stdin.readline

res = 0
s = input().strip()
stack = []
num = []
scores = {']': 3, '}': 2, ')': 1}
for i in range(len(s)-1,-1,-1):
    if s[i] in [']',')','}']:
        stack.append(s[i])
    elif s[i] in ['[','(','{']:
        stack.pop()

    else:
        tmp = 0
        for s2 in stack:
            tmp += scores[s2]
        res = max(res,tmp)
print(res)
